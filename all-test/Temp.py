from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent
import time
from _datetime import datetime

mouse = PyMouse()
key = PyKeyboard()

# def click(self, x, y, button=1, n=1):

if __name__ == '__main__':
    now = datetime.today()
    print(now.year)
    print(now.month)
    print(now.day)

    da="20170317"
    print(da[0:4]+'-'+da[4:6]+'-'+da[6:8])
