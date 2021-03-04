from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    chrome = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    # test 1
    chrome.get('https://www.baidu.com')
    chrome.save_screenshot('t1.png')

    # test 2
    scroll_width = chrome.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = chrome.execute_script('return document.body.parentNode.scrollHeight')
    chrome.set_window_size(scroll_width, scroll_height)
    chrome.save_screenshot('t2.png')

    # test 3
    chrome.get('https://help.aliyun.com/noticelist/articleid/1060248882.html')
    element = chrome.find_element_by_class_name('notice-main')
    element.screenshot(f't3.png')

    # test 4
    # test 4
    chrome.get('https://help.aliyun.com/noticelist/articleid/1060248882.html')
    scroll_width = chrome.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = chrome.execute_script('return document.body.parentNode.scrollHeight')
    chrome.set_window_size(scroll_width, scroll_height)
    chrome.get_screenshot_as_file('t4-1.png')
    element = chrome.find_element_by_class_name('notice-main')
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']
    img = Image.open('t4-1.png')
    img = img.crop((left, top, right, bottom))
    img.save('t4-2.png')

    chrome.quit()


def test():
    pass


if __name__ == '__main__':
    main()
