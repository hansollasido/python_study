import keyboard
import time
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(1)) # image_20200601_102030.png

# F9 키를 눌렀을 때 screenshot이 됨
keyboard.add_hotkey("ctrl+shift+d",screenshot) 

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행