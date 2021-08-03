from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
import datetime

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

domain = str(sys.argv[1])
url = "https://"+domain+"/"
browser.get(url)
browser.implicitly_wait(10000)
x = input("Press any key if you accepted the cookies in the browser \n")
cookies = browser.get_cookies()
for cookie in cookies:
    print("Cookie name --> ", cookie.get('name'))
    print("Cookie value --> ", cookie.get('value'))
    print("Cookie domain --> ", cookie.get('domain'))
    print("Cookie expiry --> ", datetime.datetime.fromtimestamp(cookie.get('expiry')).isoformat())

browser.close()

