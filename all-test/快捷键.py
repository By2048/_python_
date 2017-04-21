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


# http://www.cnblogs.com/pylemon/archive/2011/09/07/2169972.html
