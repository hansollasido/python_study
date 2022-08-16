import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()

# img.save("screenshot.png") 
#pyautogui.mouseInfo()
#1313,29 39,160,241 #27A0F1
# 39,160,241 은 RGB 값임

pixel = pyautogui.pixel(1313,29)
print(pixel)
# RGB 값을 반환함

print(pyautogui.pixelMatchesColor(1313,29,(39,160,241)))