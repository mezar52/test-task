import psycopg2
from config import DATABASE_URL

def init_db():
    return psycopg2.connect(DATABASE_URL)

def log_tweet(handle, tweet_text, reply_text, likes, retweets):
    conn = init_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO twitter_logs (handle, tweet_content, reply_text, likes, retweets, session_time)
        VALUES (%s, %s, %s, %s, %s, NOW());
        """,
        (handle, tweet_text, reply_text, likes, retweets)
    )
    conn.commit()
    cur.close()
    conn.close()