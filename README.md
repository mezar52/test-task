
# Twitter Auto Repost & Reply Bot

This project automates Twitter actions: it scrapes tweets, retweets the most engaging one, and replies with a short AI-generated message using Google Gemini API.

---

## Project Structure
```
├── .env                # Environment variables (credentials, keys, DB URL)
├── auth.py             # Twitter login
├── analyzer.py         # Analysis functions if used
├── config.py           # Loads config from .env
├── db.py               # Database functions 
├── main.py             # Main script to run everything
├── replier.py          # Retweet and reply logic
├── scraper.py          # Scrapes tweets
├── requirements.txt    # Python dependencies
├── schema.sql          # SQL schema file 
```

---

## Setup & Environment Configuration

### ✅ Install Python dependencies:
```bash
pip install -r requirements.txt
```

---

### ✅ Linux setup (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv chromium-driver chromium-browser
```

If using Selenium with Chromium:
```bash
sudo apt install -y chromium-chromedriver
```

> Make sure your ChromeDriver version matches your browser version.

---

### ✅ macOS setup:
1. Install Homebrew (if not installed yet):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install required tools:
```bash
brew install python chromedriver
```

> Make sure your ChromeDriver version matches your installed Chrome.

---

### ✅ Create `.env` file:
```env
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
DATABASE_URL=postgresql://user:password@localhost:5432/twitter_logs
GEMINI_API_KEY=your_gemini_api_key
```

---

### ✅ Apply SQL schema (optional):
```bash
psql -d twitter_logs < schema.sql
```

---

## How to Run the Script
```bash
python main.py
```

---

## Example Logs
```
[SCRAPER] Scraping finished. Collected tweets: 20
[REPLIER] Calling Gemini API
[REPLIER] Generated reply: "Hope it works out!"
[REPLIER] Reply sent
```

---

## SQL Schema
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

---

## ✅ Screenshots

### Tweet Scraper in Action
![Screenshot 1](./test-task1.png)

### Full Automation: Scraping, Reposting, Replying
![Screenshot 2](./test-task2.png)
