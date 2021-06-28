# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/24 14:12
"""
#标签Label
from tkinter import *
from graphicaluserinterface.person_tax_calc import person_tax_calc

def tax_calc():
    inputCount = inputVar.get()
    tax = person_tax_calc(int(inputCount))
    outputVar.set('个人所得税：%.2f 元' % tax)

root = Tk()
root.title("python GUI v1.0")
root.geometry("400x200+400+300")

topFrame = Frame(root)

inputLabel = Label(topFrame, text='请输入月收入：')
inputLabel.pack(side=LEFT, padx=5, pady= 5)

inputVar = StringVar()
inputEnter = Entry(topFrame, textvariable=inputVar)
inputEnter.pack(side=LEFT)

inputButton = Button(topFrame, text='计算', command=tax_calc)
inputButton.pack(side=LEFT, padx=5, pady= 5)
topFrame.pack(padx=5, pady=5)

outputVar = StringVar()
outputVar.set('genarel')
outputLabel = Label(root, textvariable=outputVar, font='微软雅黑 10', fg='orange')
outputLabel.pack(padx=5, pady= 5)


root.mainloop()

