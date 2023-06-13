#tkinter grid test

from tkinter import *
#linX=5
root =Tk()
root.iconbitmap("pygame.ico")
myLabel1= Label(root, text="ssda1")
myLabel2= Label(root, text="ssda2").grid(row=1, column=1)
myLabel1.grid(row=0, column=0)

ety=Entry(root, borderwidth=5,width=50, bg="black",fg="gray")
ety.grid(row=3,column=0,columnspan=2)


def mySubmit():
    #global linX
    myLableX= Label(root,text=ety.get())
    myLableX.grid()#(row=linX) 
    #linX += 1
btn=Button(root,text="submit",borderwidth=3, command=mySubmit).grid(row=3,column=2)
root.mainloop()