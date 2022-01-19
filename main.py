import time
import csv
import arabic_reshaper
from bidi.algorithm import get_display
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

# Hadless chrome browser setup
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://twitter.com/search?q=lang%3Aar")


def close():
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
            tweetItem = driver.find_element(By.XPATH, "//div[@lang='ar']")
            tweettext = tweetItem.text
            tweets = arabic_reshaper.reshape(tweettext)
            Bidi_text = get_display(tweets)
            print(tweets)

            # Csv file writing of the content of the list "tweettext
            with open("tweets.csv", "r+", encoding="utf-8") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar=',')
                csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=',')
                csvwriter.writerow(Bidi_text[::-1])

# User can interupt the program
except KeyboardInterrupt:
    close()
