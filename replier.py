import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import logging
import time
import random
import google.generativeai as genai
from config import TWITTER_USERNAME, GEMINI_API_KEY
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

logging.basicConfig(level=logging.INFO, format="[REPLIER] %(message)s")

# Gemini API config
genai.configure(api_key=GEMINI_API_KEY)


def generate_reply(tweet_text: str) -> str:
    prompt = f'Here is a tweet:\n"{tweet_text}"\nWrite a short, friendly reply in English.'
    model = genai.GenerativeModel('gemini-1.5-flash')

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        logging.info("generate_reply: attempt %d/%d", attempt, max_retries)
        delay = random.uniform(2, 4)
        logging.info("Sleeping for %.2f seconds before API call", delay)
        time.sleep(delay)

        try:
            logging.info("Calling Gemini API")
            response = model.generate_content(prompt)
            reply = response.text.strip()
            logging.info("Generated reply: %s", reply)
            return reply

        except Exception as e:
            err = str(e)
            logging.error("Gemini API exception: %s", err)
            backoff = attempt * random.uniform(1, 2)
            logging.warning("Retrying in %.2fs", backoff)
            time.sleep(backoff)

    logging.error("Failed to generate reply after %d attempts", max_retries)
    return "Sorry, I couldn't generate a reply right now."


def repost_and_reply(driver, tweet, reply_text: str):
    tweet_url = tweet.get('url')
    if not tweet_url:
        logging.error("Tweet URL missing. Can't proceed.")
        return

    try:
        logging.info("[Step 1] Opening tweet page: %s", tweet_url)
        driver.get(tweet_url)
        time.sleep(random.uniform(3, 5))

        logging.info("[Step 2] Finding retweet button")
        rt_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='retweet']"))
        )

        logging.info("[Step 3] Clicking retweet button")
        driver.execute_script("arguments[0].click();", rt_btn)

        confirm_rt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='retweetConfirm']"))
        )
        logging.info("[Step 4] Confirming retweet")
        driver.execute_script("arguments[0].click();", confirm_rt)
        logging.info("[Step 5] Retweet done")
        time.sleep(random.uniform(1, 2))

        logging.info("[Step 6] Finding reply button")
        rp_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='reply']"))
        )

        logging.info("[Step 7] Clicking reply button")
        driver.execute_script("arguments[0].click();", rp_btn)
        logging.info("[Step 8] Reply window opened")

        logging.info("[Step 9] Waiting for reply textarea")
        textarea = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid^='tweetTextarea'][contenteditable='true']")
            )
        )

        logging.info("[Step 10] Typing reply")
        for idx, ch in enumerate(reply_text, start=1):
            textarea.send_keys(ch)
            if idx % 20 == 0 or idx == len(reply_text):
                logging.info("Typed %d/%d chars", idx, len(reply_text))
            time.sleep(random.uniform(0.05, 0.15))

        logging.info("[Step 11] Finding send button")
        send_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButton']"))
        )

        logging.info("[Step 12] Sending reply")
        driver.execute_script("arguments[0].click();", send_btn)
        logging.info("[Step 13] Reply sent")

    except Exception as e:
        logging.error("Unexpected error in repost_and_reply: %s", repr(e))