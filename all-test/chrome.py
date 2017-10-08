import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome = webdriver.Chrome(chrome_path)

chrome.set_window_position(50,50) #瀏覽器位置
chrome.set_window_size(700,700) #瀏覽器大小
chrome.get("http://www.baidu.com")

elem = chrome.find_element_by_name("wd")
# elem.send_keys("selenium")
# time.sleep(3)
# elem.send_keys(Keys.RETURN)
elem.send_keys(Keys.CONTROL,'s')
# chrome.find_element_by_link_text('百度一下').click()
# chrome.quit()




# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("selenium")
# elem.send_keys(Keys.RETURN)
# assert "Google" in driver.title
# driver.close()
# driver.quit()