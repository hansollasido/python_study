import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()


# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval = 0.2) # interval은 천천히 씀
pyautogui.write("나도코딩") # 한글 처리는 안됨
pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25) 
# automate the boring stuff with python을 검색하면 찾을 수 있음

# 특수 문자
# shift 4 -> $
pyautogui.keyDown("shift")
pyautogui.press("4") 
# press는 눌렀다 떼는 동작
pyautogui.keyUp("shift")

# # 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl","alt","shift", "a")
# ctrl 누르고 > Alt 누르고 > shift 누르고 > A 누르고 > A 떼고 shift 떼고 > alt 떼고 > ctrl 떼고
pyautogui.hotkey("ctrl","a")

# 한글 넣는 법
import pyperclip 
# # 어떤 문장을 clipboard에 넣음
# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
