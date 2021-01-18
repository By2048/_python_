使用 `pywin` 模块

```py
import win32api
import win32con

# F4 115    Alt 18
win32api.keybd_event(18,0,0,0)
win32api.keybd_event(115,0,0,0)
win32api.keybd_event(115,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)

# win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
# win32api.keybd_event(86,0,0,0)  #v键位码是86
# win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
# win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

``` 



使用 `PyMouse` 模块
```py
from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent

mouse=PyMouse()
key=PyKeyboard()

# 模拟 Ctrl+S
key.press_key(key.control_key)
key.tap_key("s")
key.release_key(key.control_key)
key.tap_key(key.end_key)
```