# My Python Project

This project is organized as a Python package with modular structure:

```
.
├── assets/              # Images and resources
├── src/                 # Source code
│   ├── main.py          # Entry point
│   ├── config/          # Configuration
│   ├── db/              # Database logic
│   └── core/            # Core features: scraping, analysis, auth, reply
├── requirements.txt     # Dependencies
├── pyproject.toml       # Packaging config
└── .gitignore           # Git ignore file
```

## How to Run

```bash
cd src
python main.py
```

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

You can also package the project using:

```bash
python -m build
```