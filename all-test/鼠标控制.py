from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent
import os

mouse=PyMouse()
key=PyKeyboard()
x_dim,y_dim=mouse.screen_size()
print(x_dim,y_dim)

mouse.move(15,15)
# mouse.click(0,0,1)
# key.type_string('hello')
#
# key.press_key('Q')
# key.release_key('Q')
#
# key.tap_key(key.enter_key)

# key.tap_key('E')
# key.tap_key('K',n=2,interval=1)

# key.tap_key(key.function_keys[5]) # F5
# key.tap_key(key.numpad_keys['Home'])  # Home
# key.tap_key(key.numpad_keys[5],n=3)     # 输入 3 个 5

# Alt + Tab  快捷键
# key.press_key(key.alt_key)
# key.tap_key(key.tab_key)
# key.release_key(key.alt_key)

# key.windows_l_key

# key.press_key(['key.windows_l_key','d'])




