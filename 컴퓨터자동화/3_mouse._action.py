import pyautogui

pyautogui.sleep(3) # 3초 대기

# print(pyautogui.position())

# pyautogui.click(1386,19, duration=1) # (1386,19) 1초 동안 좌표를 마우스 클릭

# pyautogui.mouseDown() # 마우스를 클릭한 상태
# pyautogui.mouseUp() # 마우스를 뗀 상태

# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # doubleClick과 같음

# pyautogui.moveTo(300,300)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(400,400) 
# pyautogui.mouseUp() 

# pyautogui.rightClick()
# pyautogui.middleClick() # 마우스 휠

# pyautogui.moveTo(902,882)
# #pyautogui.drag(100,0) # 상대 위치, 현재 위치 기준으로 x 100만큼 움직임
# pyautogui.drag(100,0,duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될 때는 duration을 활용
# pyautogui.dragTo(702,662,duration=0.25) # 절대 위치

pyautogui.scroll(500) # 위 방향으로 300만큼 스크롤
# 양수이면 위 방향으로, 음수이면 아래 방향으로 