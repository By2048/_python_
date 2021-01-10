import time
import os

from bs4 import BeautifulSoup
from veryprettytable import VeryPrettyTable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

url = "https://www.zhihu.com/billboard"

screen_1_x, screen_1_y = 0, 0
screen_1_xx, screen_1_yy = 3840, 2160
screen_1_dpi = 2

screen_3_x, screen_3_y = 3840, 467
screen_3_xx, screen_3_yy = 4920, 2387
screen_3_dpi = 1

screen_x, screen_y = screen_3_x, screen_3_y
screen_xx, screen_yy = screen_3_xx, screen_3_yy
screen_w = screen_xx - screen_x
screen_h = screen_yy - screen_y
screen_h /= 2
screen_dpi = screen_3_dpi

w = screen_w * (5 / 6) / screen_dpi
h = screen_h * (8 / 9) / screen_dpi
x = screen_x + (screen_w - w) / 2
y = screen_y + (screen_h - h) / 2
x /= 2
y /= 2
w, h, x, y = int(w), int(h), int(x), int(y)

chrome_options: Options = Options()
chrome_options.add_argument(f'--window-size={w},{h}')
chrome_options.add_argument(f'--window-position={x},{y}')

executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome: WebDriver = webdriver.Chrome(
    executable_path=executable_path, chrome_options=chrome_options,
    service_log_path=os.devnull
)
chrome.minimize_window()

chrome.get(url)
time.sleep(3)

response: str = chrome.page_source
data = BeautifulSoup(response, "html.parser")

index: int = 0
table: VeryPrettyTable = VeryPrettyTable("index tittle metrics".split())
table.align["tittle"] = "l"
for hot_item in data.find_all("a", class_="HotList-item"):
    index += 1
    tittle = hot_item.find("div", class_="HotList-itemTitle").get_text()
    try:
        content = hot_item.find("div", class_="HotList-itemExcerpt").get_text()
    except Exception as e:
        content = ""
    metrics = hot_item.find("div", class_="HotList-itemMetrics").get_text()
    metrics = metrics.replace(" ", "").replace("万热度", "")
    table.add_row([str(index).zfill(2), tittle, metrics])

print(table.get_string())

chrome.close()
