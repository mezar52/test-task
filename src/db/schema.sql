CREATE TABLE IF NOT EXISTS twitter_logs (
    id SERIAL PRIMARY KEY,
    handle VARCHAR(50) NOT NULL,
    session_time TIMESTAMP NOT NULL DEFAULT NOW(),
    tweet_content TEXT NOT NULL,
    reply_text TEXT NOT NULL,
    likes INTEGER NOT NULL,
    retweets INTEGER NOT NULL
);
