import time
from pprint import pprint

from selenium import webdriver

chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

chrome = webdriver.Chrome(executable_path=chrome_driver)

chrome.set_window_size(100, 300)

chrome.get('http://www.baidu.com')

source = chrome.page_source
pprint(source)

time.sleep(3)

chrome.close()
chrome.quit()
