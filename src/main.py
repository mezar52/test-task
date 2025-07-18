import logging
from src.handlers.auth import create_driver, login
from src.handlers.scraper import scrape_tweets
from src.handlers.analyzer import select_top_tweet
from src.handlers.replier import generate_reply, repost_and_reply
from src.db.db import log_tweet
from src.core.config import TWITTER_USERNAME

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )
    driver = create_driver()
    try:
        login(driver)
        logging.info(f"Logged in as @{TWITTER_USERNAME}")
        tweets = scrape_tweets(driver, count=20)
        logging.info(f"Scraped {len(tweets)} tweets")
        top = select_top_tweet(tweets)
        logging.info(f"Top tweet: {top['text']}")
        reply = generate_reply(top['text'])
        logging.info(f"Reply: {reply}")
        repost_and_reply(driver, top, reply)
        log_tweet(
            "@" + TWITTER_USERNAME,
            top['text'], reply,
            top['likes'], top['retweets']
        )
        logging.info("Actions logged to DB successfully")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
