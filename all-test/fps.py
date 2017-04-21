from PIL import Image
from PIL import ImageGrab
import time

im = Image.open('f:\\2.jpg')
rgb_im = im.convert('RGB')
# 400 400
r, g, b = rgb_im.getpixel((1, 1))

print(r)
print(g)
print(b)

cnt = 0
for i in range(3000):
    im = ImageGrab.grab()
    im.save("f:\\Test\\" + str(cnt)+".jpg")
    print("f:\\Test\\" + str(cnt) + ".jpg")
    cnt+=1
    # time.sleep(10)
