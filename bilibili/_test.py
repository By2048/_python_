from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"


chrome = webdriver.Chrome(chrome_path)
chrome.set_window_position(50,50)
chrome.set_window_size(1300,1000)

# 使用百度进行搜索  1)找到元素,2)发送按键
bd_link='http://www.baidu.com'
chrome.get(bd_link)

time.sleep(3)
js='window.open("https://www.sogou.com");'
chrome.execute_script(js)