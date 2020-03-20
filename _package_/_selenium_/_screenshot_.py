from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_1():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    chrome = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    chrome.set_window_size(1920, 1080)
    # scroll_width = chrome.execute_script('return document.body.parentNode.scrollWidth')
    # scroll_height = chrome.execute_script('return document.body.parentNode.scrollHeight')
    # chrome.set_window_size(scroll_width, scroll_height)
    url = f'https://help.aliyun.com/noticelist/articleid/1060248882.html'
    chrome.get(url)
    element = chrome.find_element_by_class_name('notice-main')
    element.screenshot(f'image.png')
    chrome.quit()


if __name__ == '__main__':
    test_1()
