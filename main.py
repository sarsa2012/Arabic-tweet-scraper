import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

filename = "Tweet_Scrapes.csv"

driver = webdriver.Chrome()
driver.get("https://twitter.com/search?q=lang%3Aar")
array = []


def close():
    driver.close()


try:
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(7)  # sleep_between_interactions
        tweetscope = driver.find_elements(By.TAG_NAME, "article")
        for items in tweetscope:
            tweetItem = driver.find_element(By.XPATH, "//div[@lang='ar']")
            array.append(tweetItem)
except KeyboardInterrupt:
    close()
