from tkinter import *

root = Tk()
root.title("Nado GUI") # 창 제목
root.geometry("640x480") # 가로 * 세로 크기

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1~31 일
    listbox.insert(END,str(i)+"일") # 1일,2일, ...
listbox.pack(side="left")

# 아래 코드가 없으면 맵핑이 안됨
scrollbar.config(command=listbox.yview)


root.mainloop() # 창이 닫히지 않도록 함