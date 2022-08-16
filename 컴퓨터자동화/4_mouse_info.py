import pyautogui
#pyautogui.mouseInfo() mouse 정보를 볼 수 있음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
#pyautogui.FAILSAFE = False # 사용자가 실행중 마우스를 옮겨도 끝나지 않음


for i in range(5) :
    pyautogui.move(100,100)
    