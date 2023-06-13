#testlabel
from cgitb import text
from tkinter import *
win= Tk()
def changme():
    myssLabel['text']="omg"

global myssLabel
myssLabel= Label(win, text="me").pack()
btn=Button(win, text="change", command=changme).pack()
win.mainloop()