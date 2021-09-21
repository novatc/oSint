from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
import pandas as pd

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

domain = str(sys.argv[1])
url = "https://"+domain+"/"
browser.get(url)
cookies_before = browser.get_cookies()
x = input("Press any key if you accepted the cookies in the browser \n")
cookies_after = browser.get_cookies()

cookie_after_df = pd.DataFrame(cookies_after)
cookies_before_df = pd.DataFrame(cookies_before)


cookie_after_df.to_html("cookies_with_consent.html")
cookies_before_df.to_html("cookies_without_consent.html")
browser.close()

