import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.config.config import TWITTER_USERNAME, TWITTER_PASSWORD


def create_driver():
    # Auto-downloads the correct ChromeDriver version
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


def type_like_human(element, text, min_delay=0.4, max_delay=1.2):
    # Types text with random delay between keystrokes
    for ch in text:
        element.send_keys(ch)
        time.sleep(random.uniform(min_delay, max_delay))


def login(driver):
    driver.get("https://twitter.com/login")
    wait = WebDriverWait(driver, 30)

    # Step 1: enter username/email/phone
    user_input = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
    type_like_human(user_input, TWITTER_USERNAME)
    user_input.send_keys(Keys.ENTER)

    # Step 2: enter password
    pwd_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    type_like_human(pwd_input, TWITTER_PASSWORD)
    pwd_input.send_keys(Keys.ENTER)

    # Wait for redirect to home page
    wait.until(EC.url_contains("home"))
    time.sleep(random.uniform(3, 6))
