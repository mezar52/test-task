import time
import random
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="[SCRAPER] %(message)s")

DEBUG_MODE = False  # set True if you want full error details for debugging


def parse_count(text: str) -> int:
    t = text.strip().upper()
    try:
        if t.endswith('K'):
            return int(float(t[:-1].replace(',', '.')) * 1_000)
        if t.endswith('M'):
            return int(float(t[:-1].replace(',', '.')) * 1_000_000)
        return int(t.replace(',', ''))
    except ValueError:
        logging.warning(f"Failed to parse number: '{text}', using 0 instead")
        return 0


def accept_cookies_if_present(driver):
    try:
        logging.info("Checking for 'Accept all cookies' button...")
        accept_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Accept all cookies')]/ancestor::button"))
        )
        driver.execute_script("arguments[0].click();", accept_btn)
        logging.info("Accepted cookies")
        time.sleep(2)
    except Exception:
        logging.info("No cookie button found or already accepted")


def scrape_tweets(driver, count=20):
    accept_cookies_if_present(driver)

    tweets = []
    attempts = 0
    max_attempts = 15

    while len(tweets) < count and attempts < max_attempts:
        elems = driver.find_elements(By.CSS_SELECTOR, "article[data-testid='tweet']")
        logging.info(f"Found {len(elems)} tweets on the page")

        for el in elems:
            if len(tweets) >= count:
                break
            try:
                # slight delay to keep things stable
                time.sleep(random.uniform(0.1, 0.3))

                text_el = el.find_element(By.CSS_SELECTOR, "div[data-testid='tweetText']")
                text = text_el.text.strip()

                if not text:
                    logging.info("Skipped tweet with no text")
                    continue

                tweet_url_el = el.find_element(By.CSS_SELECTOR, "a[href*='/status/']")
                tweet_url = tweet_url_el.get_attribute("href")

                if any(t['url'] == tweet_url or t['text'] == text for t in tweets):
                    logging.info("Skipped duplicate tweet")
                    continue

                like_txt = el.find_element(By.CSS_SELECTOR, "button[data-testid='like']").text or "0"
                rt_txt = el.find_element(By.CSS_SELECTOR, "button[data-testid='retweet']").text or "0"
                likes = parse_count(like_txt)
                retweets = parse_count(rt_txt)

                tweets.append({
                    'element': el,
                    'text': text,
                    'likes': likes,
                    'retweets': retweets,
                    'url': tweet_url
                })

                logging.info(f"Tweet #{len(tweets)} collected: {text[:30]}...")

            except Exception as e:
                if DEBUG_MODE:
                    logging.exception("Error while processing tweet")
                else:
                    logging.info("Skipped tweet: missing text element (probably ad or special block)")
                continue

        if len(tweets) < count:
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            attempts += 1
            logging.info(f"Scrolling... attempt {attempts}/{max_attempts}")
            time.sleep(random.uniform(1, 2))

    logging.info(f"Scraping finished. Collected tweets: {len(tweets)}")
    return tweets[:count]