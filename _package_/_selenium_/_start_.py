import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

screen_x = 0
screen_y = 0
screen_xx = 3840
screen_yy = 2160
screen_dpi = 2
screen_w = screen_xx - screen_x
screen_h = screen_yy - screen_y

w = screen_w * (5 / 6)
h = screen_h * (8 / 9)
x = screen_x + (screen_w - w) / 2
y = screen_y + (screen_h - h) / 2

x = x / screen_dpi
y = y / screen_dpi
w = w / screen_dpi
h = h / screen_dpi

x, y, w, h = int(x), int(y), int(w), int(h)

options = Options()
options.add_argument(f'--window-size={w},{h}')
options.add_argument(f'--window-position={x},{y}')

browser = webdriver.Chrome(
    executable_path=driver_path,
    chrome_options=options,
    service_log_path=os.devnull
)

browser.get("www.baidu.com")
browser.implicitly_wait(10)

source = browser.page_source

browser.switch_to.frame(0)
browser.switch_to.frame(0)

element_video = browser.find_element_by_tag_name("video")
download_url = element_video.get_attribute("src")

browser.set_window_size(100, 300)
browser.get_window_size()
browser.get_window_position()

browser.minimize_window()
browser.maximize_window()
browser.close()
browser.quit()
