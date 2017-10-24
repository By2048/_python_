from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

# #phantomjs 需要改动下
# driver = webdriver.Firefox()
# driver.get("http://login.taobao.com")
# #windows 用Keys.CONTROL 如同ctrl+t
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# driver.get('http://mm.taobao.com/')
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
# driver.close()


chrome = webdriver.Chrome(chrome_path)
chrome.get('http://www.baidu.com')
time.sleep(3)
# chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
# ActionChains(chrome).send_keys(Keys.CONTROL+'t').perform()
js="window.open('http://www.sohu.com')"
chrome.execute_script(js)
# time.sleep(3)
# chrome.get('http://www.google.com')
# chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# chrome.get('http://www.sohu.com')
# chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# chrome.get('http://www.bing.com')
