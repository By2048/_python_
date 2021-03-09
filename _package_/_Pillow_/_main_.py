import os
import time

from PIL import Image
from PIL import ImageGrab


def get_screen_rgb(img_path):
    """获取图片指定点的像素
    """
    img = Image.open(img_path)
    img_rgb = img.convert('RGB')
    r, g, b = img_rgb.getpixel((1, 1))
    print(r, g, b)


def get_screenshot():
    """屏幕截图
    """
    img_path = r't:\_tmp'
    now_time = time.localtime(time.time())
    names = [str(now_time.tm_hour), str(now_time.tm_min), str(now_time.tm_sec), '.jpg']
    img_name = "_".join(names)
    img = ImageGrab.grab()
    img.save(os.path.join(img_path, img_name))


get_screen_rgb('T:\\1.png')
get_screenshot()
