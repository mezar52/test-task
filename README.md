# Twitter Scraper & Responder 🤖

A Python-based tool that logs into Twitter, scrapes tweets, analyzes them, and auto-generates replies based on engagement metrics.

---

## 📁 Project Structure

```
.
├── assets/               # Screenshots / examples
│   ├── test-task1.png
│   └── test-task2.png
├── src/                  # Source code
│   ├── main.py           # Entry point
│   ├── core/             # Config and constants
│   │   └── config.py
│   ├── db/               # Database handler
│   │   ├── db.py
│   │   └── schema.sql
│   └── handlers/         # All app logic
│       ├── analyzer.py
│       ├── auth.py
│       ├── replier.py
│       └── scraper.py
├── .env.example          # Example environment file
├── requirements.txt      # Python dependencies
├── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Set up a virtual environment (recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Rename `.env.example` → `.env` and provide the following values:

```env
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
DATABASE_URL=postgresql://username:password@localhost:5432/your_database
GEMINI_API_KEY=your_google_gemini_api_key
```

These are loaded automatically via `dotenv`.

---

## 💽 Database

This project uses **PostgreSQL**. Make sure your database is created and accessible at the `DATABASE_URL` you provide in the `.env`.

Schema is located at `src/db/schema.sql`:

```sql
CREATE TABLE IF NOT EXISTS tweets (
    id SERIAL PRIMARY KEY,
    username TEXT,
    original TEXT,
    reply TEXT,
    likes INTEGER,
    retweets INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Run the project

```bash
cd src
python main.py
```

This will:
- Log into Twitter
- Scrape tweets from your timeline
- Pick the top tweet based on engagement
- Auto-generate a reply using Gemini API
- Post the reply and log it in the database

---

## 🖼 Example Screenshots

### 🔹 Before Replying
![Before](assets/test-task1.png)

### 🔹 Auto-generated Reply
![After](assets/test-task2.png)

---

## 🧪 Tested on

- ✅ Windows 10 / 11
- ✅ macOS Ventura / M1
- ✅ Ubuntu 22.04 LTS

---

## 🛠 Dependencies

- `selenium`
- `webdriver-manager`
- `python-dotenv`
- `psycopg2` *(PostgreSQL adapter)*
- `openai` or `google-generativeai` *(depending on which Gemini API library you use)*

Install them with:

```bash
pip install -r requirements.txt
```

---
