使用 selenium 模块来控制 Chrome

[selenium 官方文档](http://selenium-python.readthedocs.io/)

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 ChromeDriver 的路径
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

start_url = 'http://h.bilibili.com/eden/draw_area#/all/hot'

chrome = webdriver.Chrome(chrome_path)
chrome.set_window_position(50, 50)
chrome.set_window_size(1300, 1000)

chrome.get(start_url)   # 使用Chrome打开页面

# 使用百度进行搜索  1)找到元素,2)发送按键
bd_link = 'http://www.baidu.com'
chrome.get(bd_link)
elem = chrome.find_element_by_id('kw')
elem.send_keys(u'需要搜索的内容')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')  # 全选输入框的内容
elem.send_keys(Keys.ENTER)

# 对窗体属性进行判断
assert "Python" in chrome.title

# 获取 chrome 的当前 url
print(chrome.current_url)

# 输出当前页的 title
print(chrome.title)

# 窗体发送 Ctrl+A
ActionChains = webdriver.common.action_chains.ActionChains
ActionChains(chrome).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# 保存网页到本地
with open('E:\\desktop\\bilbili.html', 'w', encoding='utf-8') as f:
    f.write(chrome.page_source)

# 保存网页的截图到本地
chrome.save_screenshot('E:\\Desktop\\screenshot.png')

# 退出页面
chrome.close()

# 退出Chrome
chrome.quit()

# 打开一个页面
bd_link = 'http://www.baidu.com'
chrome.get(bd_link)

# 使用 js 打开页面
js="window.open('http://www.sohu.com')"
chrome.execute_script(js)

# 窗体所有的句柄
handles = chrome.window_handles
# 如果打开多个浏览器句柄和标签页的对应关系：
# 标签页顺序（按照打开顺序）：1 2 3 4 5
# 对应的句柄 ：0 4 3 2 1

# 切换窗体
chrome.switch_to.window(handles[1])

```