import os
import time

from ahk import AHK

os.environ['AHK_PATH'] = r"D:\AutoHotkey\AutoHotkey.exe"

ahk = AHK()

# ahk.click()

# ahk.right_click()


time.sleep(3)
ahk.send("^c")

# ahk.mouse_move(100, 100, speed=10, relative=True)  # Moves the mouse reletave to the current position
# ahk.mouse_position = (100, 100)  # Moves the mouse instantly to absolute screen position
# ahk.click()  # Click the primary mouse button
# ahk.double_click() # Clicks the primary mouse button twice
# ahk.click(200, 200)  # Moves the mouse to a particular position and clicks
# ahk.right_click() # Clicks the secondary mouse button
# ahk.mouse_drag(100, 100, relative=True) # Holds down primary button and moves the mouse
