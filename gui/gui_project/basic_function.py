from tkinter import filedialog
import tkinter.ttk as ttk 
from tkinter import *

def add_file():
    from tkinter import filedialog

    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir="C:/") # 최초에 C:/ 경로를 보여줌
    # 사용자가 선택한 파일 목록
    for file in files:
        #list_file.insert(END,file)
        pass