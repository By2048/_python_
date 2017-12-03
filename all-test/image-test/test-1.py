from PIL import Image

import glob

import os

im = Image.open("F:/_Test/Pillow/1.jpg")

# print(im.format, im.size, im.mode)
# JPEG (1920, 1080) RGB

# im.show()


# 创建缩略图
size = (128,128)
for infile in glob.glob("F:/_Test/Pillow/*.jpg"):
    f, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size,Image.ANTIALIAS)
    img.save(f+".thumbnail","JPEG")



