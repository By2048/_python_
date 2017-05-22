import win32api
import win32con
# F4 115    Alt 18
# 按下 Alt+F4
win32api.keybd_event(18,0,0,0)
win32api.keybd_event(115,0,0,0)
win32api.keybd_event(115,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)

