#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent
import time
import win32api
import win32con


mouse=PyMouse()
key=PyKeyboard()

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get("https://www.baidu.com")


#
# #输入框输入内容
driver.find_element_by_id("kw").send_keys("lol")
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
# time.sleep(3)
# #使用组合键ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# time.sleep(3)
# #使用组合键ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# time.sleep(3)
# #输入框重新输入内容，搜索
# #输入框输入中文问题：
# # selenium2 python在send_keys()中输入中文一直报错，其前面加个小u 就解决了：
# #即：send_keys(u"输入中文")
# driver.find_element_by_id("kw").send_keys(u"虫师cnblogs")
# driver.find_element_by_id("su").click()
# with open('E:\desktop\zhihu.html','w',encoding='utf-8') as f:
#     f.write(driver.page_source)  #保存网页到本地


time.sleep(3)

# time.sleep(5)
# driver.quit()
print('1')
key.press_key(key.control_key)
print('2')
key.tap_key("s")
print('3')
time.sleep(3)
key.release_key(key.control_key)
time.sleep(1)
key.tap_key(key.end_key)

# time.sleep(3)
# driver.find_element_by_id('kw').send_keys((Keys.CONTROL, 's'))

# ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# ActionChains(driver).key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()


driver.save_screenshot('e:\\desktop\\test-in.png')