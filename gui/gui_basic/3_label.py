from tkinter import *

root = Tk()

root.title("Nado GUI") # 창 제목

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # 전역 변수로 설정하지 않으면 지역함수 특성상 반영이 안될 수 있음
    photo2 = PhotoImage(file="gui_basic/img2.png") 
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop() # 창이 닫히지 않도록 함
