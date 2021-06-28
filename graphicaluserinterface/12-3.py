# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/24 14:12
"""
#标签Label
from tkinter import *

root = Tk()
root.title("python GUI v1.0")
root.geometry("400x200+400+300")

inputLabel = Label(root, text='重操旧业', bg='lightblue', font='微软雅黑 12 normal')
inputLabel.pack(padx=5, pady= 10, fill=X)

inputLabel = Label(root, text='重操旧业', bg='lightyellow', font='微软雅黑 12 normal')
inputLabel.pack(padx=5, pady= 10, fill=BOTH, expand=True)


root.mainloop()

