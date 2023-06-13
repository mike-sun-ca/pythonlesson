#testGameMove

import time
from tkinter import *
from turtle import forward, width

tk=Tk()
myForwardX=1
myForwardY=1
tk.iconbitmap("pygame.ico")
tk.title("Space Man game")

def moveGraph(event):
    if event.keysym=="Up":
        canvas.move(meSquareHandle,0,-3)
    elif event.keysym=="Down":
        canvas.move(meSquareHandle,0,3)
    elif event.keysym=="Left":
        canvas.move(meSquareHandle,-3,0)
    elif event.keysym=="Right":
        canvas.move(meSquareHandle,3,0)
    else:
        tk.quit()

canvas =Canvas(tk, width=500, height=500)
canvas.pack()
meSquareHandle=canvas.create_rectangle(200,430,300, 460, fill="black")
robotImage=PhotoImage(file="robotspace50.gif")
spritHandle= canvas.create_image(10,10,image=robotImage)

canvas.bind_all('<KeyPress-Up>',moveGraph)
canvas.bind_all('<KeyPress-Down>',moveGraph)
canvas.bind_all('<KeyPress-Left>',moveGraph)
canvas.bind_all('<KeyPress-Right>',moveGraph)
canvas.bind_all('<KeyPress-q>',moveGraph)

# myExitButton=Button(tk,text="Exit", command=tk.quit)
# myExitButton.pack()
while 1:
    #canvas.move(spritHandle,5,5)
    # tk.title(canvas.coords(spritHandle))
    mycoords=canvas.coords(spritHandle)
    myX, myY =mycoords
    tk.title(myX)
    if myX > 470 :
        myForwardX=-1
    if myY > 400 :
        myForwardY=-1
    if myX < 30  :
        myForwardX=1
    if myY < 30 :
        myForwardY=1
    canvas.coords(spritHandle, myX+myForwardX*3, myY +myForwardY*3)

    tk.update()
    time.sleep(0.02)

tk.mainloop()