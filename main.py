import time
import csv
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

# Hadless chrome browser setup
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://twitter.com/search?q=lang%3Aar")


tweets = []

def close():
    dict = {'tweet': tweets}
    df = pd.DataFrame(dict).drop_duplicates()
    df.to_csv('tweets.csv', index=False, encoding='utf-8', mode='a', header=False)
    driver.close()


try:
    while True:

        # Scrolling
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)  # sleep_between_interactions

        # First scope of search by Elements
        tweetscope = driver.find_elements(By.TAG_NAME, "article")

        # Looping inside the Element to extract Arabic text
        for items in tweetscope:
            tweet = driver.find_element(By.XPATH, "//div[@lang='ar']").text
            tweets.append(tweet)

# User can interupt the program
except KeyboardInterrupt:
    close()
