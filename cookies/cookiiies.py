from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

url = str(sys.argv[1])

browser.get(url)
browser.implicitly_wait(10000)
x = input("pls wait")
cookies = browser.get_cookies()
for cookie in cookies:
    print(cookie)

browser.close()

