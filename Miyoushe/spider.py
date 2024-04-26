import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


login_url = "https://www.miyoushe.com/sr/"
username = "18632335705"
password = "1qaz2wsx"
browser = webdriver.Edge()
def login():
    browser.get(login_url)
    time.sleep(10)
    # 定位到关闭图标元素并点击
    close_icon = browser.find_element(By.CLASS_NAME, 'close')
    close_icon.click()

    # 定位到头像链接元素并点击
    avatar_link = browser.find_element(By.CSS_SELECTOR, '.header__avatar')
    avatar_link.click()

if __name__ == '__main__':
    login()