import tkinter.ttk as ttk 
from tkinter import *


root = Tk()

root.title("Nado GUI") # 창 제목
root.geometry("640x480") # 가로 * 세로 크기

values=[str(i) + "일" for i in range(1,32)] # 1 ~ 31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # 목록이 5개 까지 밖에 안보임
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 목록 10개까지 보임
readonly_combobox.current(0) # 최초 목록 
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get()) # 선택된 값 표시

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop() # 창이 닫히지 않도록 함