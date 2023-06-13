#entry test
from tkinter import *
root= Tk()
root.iconbitmap("pygame.ico")
#root.wm_iconbitmap()
e=Entry(root,width=50)
e.pack()

def mySubmit():
    myLabel= Label(root, text="Hello "+ e.get())
    myLabel.pack()

btn=Button(root,text="submit", command=mySubmit)
btn.pack()
root.mainloop()