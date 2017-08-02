from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent

import time
import win32api
import win32con


mouse=PyMouse()
key=PyKeyboard()

x_dim,y_dim=mouse.screen_size()

if __name__=='__main__':
    time.sleep(5)
    for num in range(8):
        print("Num "+str(num))
        key.tap_key(chr(49 + num))
        mouse.press(2880, 551, 1)
        time.sleep(300)



    # key.tap_key('e')
    # time.sleep(1)
    # for tmp in range(8):
    #     mouse.move(2590 + tmp * 75, 585)
    #     time.sleep(1)
    #     mouse.click(2590 + tmp * 75, 585, 1, 1)
    #     print('---')
    #     mouse.move(2590 + tmp * 75, 820)
    #     time.sleep(1)
    #     mouse.click(2590 + tmp * 75, 820, 1, 1)
    # time.sleep(1)
    # key.tap_key("e")


# key.press_key(key.shift_key)
# time.sleep(3)
#
# key.tap_key("e")
# for num in range(8):
#     mouse.click(2590+num*75,585,1,1)
#     mouse.click(2590+num*75,820,1,1)
# key.tap_key("e")


