import pyautogui

# file_menu = pyautogui.locateOnScreen("terminal_menu.png")

# print(file_menu)

# # pyautogui.click(file_menu)
# pyautogui.moveTo(file_menu)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 못 찾으면 none으로 반환함
# 이미지가 조금만 바껴도 민감하게 바뀜


# 똑같은 이미지 다 찾아서 클릭함
# for i in pyautogui.locateAllOnScreen('checkbox.png'):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# file_menu = pyautogui.locateOnScreen("terminal_menu.png")
# pyautogui.moveTo(file_menu)

# 시간이 오래 걸림
# 속도 개선
# 1. GrayScale
# 정확도 떨어질 수 있음
# file_menu = pyautogui.locateOnScreen("terminal_menu.png",grayscale=True)
# pyautogui.moveTo(file_menu)


# 2. 범위 지정
# file_menu = pyautogui.locateOnScreen("terminal_menu.png", region=(1270,1,710,76))
# pyautogui.moveTo(file_menu)

# 3. 정확도 조정
# 이미지가 똑같진 않지만 이정도 퍼센트 되면 되는 걸로 
# confidence는 정확도
# run_btn = pyautogui.locateOnScreen('run_btn.png',confidence=0.7)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# if나 while을 씀
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (Timeout)

import time
import sys
timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#      file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#      end = time.time() # 종료 시간 설정

#      if end-start > timeout:
#          print("시간 종료")
#          sys.exit()

# pyautogui.click(file_menu_notepad)
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png",10)

