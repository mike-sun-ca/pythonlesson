import sys, time
from tkinter import *

from traceback import format_stack
#from tkinter import ttk

tk=Tk()
tk.iconbitmap("pygame.ico")
#frm=ttk.Frame(tk,padding=10)
#frm.grid()
def moveGraph(event):
    if event.keysym=="Up":
        canvas.move(canvasHandle,0,-3)
    elif event.keysym=="Down":
        canvas.move(canvasHandle,0,3)
    elif event.keysym=="Left":
        canvas.move(canvasHandle,-3,0)
    else:
        canvas.move(canvasHandle,3,0)

def exitMe():
    print("OMG")
    #sys.exit()
    tk.destroy()
e=Entry(tk)
e.pack()

def mySubmit():
    myLable=Label(tk,text=e.get())
    myLable.pack()

tk.title("Let's play game")
canvas =Canvas(tk, width=500, height=500)

canvas.pack()

#https://tkdocs.com/shipman/
canvasHandle=canvas.create_polygon(10,10,10,60,60,60,60,10,fill="red")
arcHandle=canvas.create_arc(10,10,50,50, fill="yellow")
lineHandle=canvas.create_line(30,50,60,50,100,10,arrow=BOTH,fill="gray")
ovalHandle=canvas.create_oval(150,150,300,200,fill="pink", outline="green", activefill="blue")
textHandle=canvas.create_text(170,20,fill="purple",text="Look at me")
bitmapInfoHanle=canvas.create_bitmap(180,50,bitmap="info")
bitmapErrHanle=canvas.create_bitmap(180,100,bitmap="error")
bitmapQuestionHanle=canvas.create_bitmap(180,150,bitmap="question")
canvas.itemconfig(canvasHandle,fill="blue")
btn1= Button(tk, text="Exit", command=exitMe)
#btn.grid()

btn1.pack()
btn2=Button(tk,text="Exit", command=tk.quit)
btn2.pack()
btnAdd= Button(tk, text="Submit", command=mySubmit)
btnAdd.pack()

canvas.move(canvasHandle,200,0)
canvas.bind_all('<KeyPress-Up>',moveGraph)
canvas.bind_all('<KeyPress-Down>',moveGraph)
canvas.bind_all('<KeyPress-Left>',moveGraph)
canvas.bind_all('<KeyPress-Right>',moveGraph)


tk.mainloop()
