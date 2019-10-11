import time

from selenium import webdriver

dev = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

chrome = webdriver.Chrome(executable_path=dev)
time.sleep(5)
chrome.quit()
