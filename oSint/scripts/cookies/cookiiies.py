from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
import pandas as pd

def start_browser():
    binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary)
    return browser


def get_cookies(browser, urls: list):
    urls = list(urls)
    final_cookies = []
    for url in urls:
        browser.get(url)
        cookies = browser.get_cookies()
        for cookie in cookies:
            if cookie not in final_cookies:
                final_cookies.append(cookie)

    return final_cookies

def scrape_cookies(base_url, urls):
    browser = start_browser()

    browser.get(base_url)
    cookies_before = get_cookies(browser, urls)

    browser.get(base_url)

    x = input("Press any key if you accepted the cookies in the browser \n")
    
    cookies_after = get_cookies(browser, urls)

    cookies_after_df = pd.DataFrame(cookies_after)
    cookies_before_df = pd.DataFrame(cookies_before)

    browser.close()

    return cookies_before_df.to_html(), cookies_after_df.to_html()
