# Twitter Auto Repost & Reply Bot

This project automates Twitter actions: it scrapes tweets, retweets the most engaging one, and replies with a short AI-generated message using Google Gemini API.

---

##  Project Structure
```
├── .env                # Environment variables (credentials, keys, DB URL)
├── auth.py             # Twitter login
├── analyzer.py         # (Optional, analysis functions if used)
├── config.py           # Loads config from .env
├── db.py               # Database functions (optional)
├── main.py             # Main script to run everything
├── replier.py          # Retweet and reply logic
├── scraper.py          # Scrapes tweets
├── requirements.txt    # Python dependencies
├── schema.sql          # SQL schema file (optional)
```

---

##  Setup & Environment Configuration

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file (already included in your project):
```env
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
DATABASE_URL=postgresql://user:password@localhost:5432/twitter_logs
GEMINI_API_KEY=your_gemini_api_key
```

3. (Optional) Apply SQL schema if using the database:
```bash
psql -d twitter_logs < schema.sql
```

---

##  How to Run the Script
```bash
python main.py
```

---

##  Example Logs
```
[SCRAPER] Scraping finished. Collected tweets: 20
[REPLIER] Calling Gemini API
[REPLIER] Generated reply: "Hope it works out!"
[REPLIER] Reply sent
```

---

##  SQL Schema
```sql
CREATE TABLE IF NOT EXISTS twitter_logs (
    id SERIAL PRIMARY KEY,
    handle VARCHAR(50) NOT NULL,
    session_time TIMESTAMP NOT NULL DEFAULT NOW(),
    tweet_content TEXT NOT NULL,
    reply_text TEXT NOT NULL,
    likes INTEGER NOT NULL,
    retweets INTEGER NOT NULL
);
```
## Screenshots

### Tweet Scraper in Action
![Screenshot 1](./test-task1.png)

### Full Automation: Scraping, Reposting, Replying
![Screenshot 2](./test-task2.png)
