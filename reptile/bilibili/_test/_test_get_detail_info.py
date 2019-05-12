from selenium import webdriver

try:
    from conf import *
    from download import *
    from sql import *
    from tool import *
    from image import *
except ImportError:
    from bilibili.config import *
    from bilibili.download import *
    from bilibili.sql import *
    from bilibili.tool import *
    from bilibili.image import *

chrome = webdriver.Chrome(chrome_path)
chrome.set_window_position(100, 50)
chrome.set_window_size(1300, 1000)

detail_links=['http://h.bilibili.com/706161','http://h.bilibili.com/546947']

chrome.get('http://www.baidu.com')

def open_detail_link(links):
    for link in links:
        js = "window.open('{0}')".format(link)
        chrome.execute_script(js)

def get_other_info(handle):
    chrome.switch_to.window(handle)
    images=chrome.find_element_by_class_name('images')
    imgs=images.find_elements_by_tag_name('img')
    if len(imgs)==0:
        return
    else:
        for img in imgs:
            down_link=img.get_attribute('src')
            name=os.path.basename(down_link)
            print(down_link)
            print(name)
            # bili_img.name.append(name)
            # bili_img.down_link.append(down_link)
            # bili_img.num+=1
    chrome.close()
    return bili_img


open_detail_link(detail_links)

handles=chrome.window_handles
for _handle in handles[1:]:
    get_other_info(_handle)



# elem.click()
# time.sleep(3)
# chrome.switch_to.window(chrome.window_handles[1])
# print(chrome.title)
# time.sleep(3)
# chrome.close()
# time.sleep(1)














