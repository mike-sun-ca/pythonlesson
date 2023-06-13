#testGameMove


import time
from tkinter import *
from tkinter import messagebox


tk=Tk()
myForwardX=1
myForwardY=1
myScore=0
tk.iconbitmap("pygame.ico")
tk.title("Space Man game")

def moveGraph(event):
    if event.keysym=="Up":
        canvas.move(meSquareHandle,0,-3)
    elif event.keysym=="Down":
        canvas.move(meSquareHandle,0,3)
    elif event.keysym=="Left":
        canvas.move(meSquareHandle,-6,0)
    elif event.keysym=="Right":
        canvas.move(meSquareHandle,6,0)
    else:
        tk.destroy()

canvas =Canvas(tk, width=500, height=500)
canvas.pack()
meSquareHandle=canvas.create_rectangle(200,430,300, 460, fill="black")
robotImage=PhotoImage(file="robotspace50.gif")
spritHandle= canvas.create_image(10,10,image=robotImage)
scoreText=StringVar()
scoreText.set("Your score:")
myLabel = Label(tk, textvariable=scoreText ).pack()
btn= Button(tk,text="exit", command=tk.quit).pack()


canvas.bind_all('<KeyPress-Up>',moveGraph)
canvas.bind_all('<KeyPress-Down>',moveGraph)
canvas.bind_all('<KeyPress-Left>',moveGraph)
canvas.bind_all('<KeyPress-Right>',moveGraph)
canvas.bind_all('<KeyPress-q>',moveGraph)

# myExitButton=Button(tk,text="Exit", command=tk.quit)
# myExitButton.pack()
def moveIt():
    global myForwardX, myForwardY, myScore 
    #canvas.move(spritHandle,5,5)
    # tk.title(canvas.coords(spritHandle))
    mycoords=canvas.coords(spritHandle)
    myX, myY =mycoords
    collisionObjList = canvas.find_overlapping(myX-25, myY-25, myX+25, myY+25)
    #tk.title(collisionFlag)
    if meSquareHandle in collisionObjList:
        myForwardY=-1
        myScore += 1
        scoreText.set("Your score: "+ str(myScore))
        


    #tk.title(myX)
    if myX > 470 :
        myForwardX=-1
    if myY > 450 :
        #myForwardY=-1
        messagebox.showerror(title="VanLan Game Class", message="Game over")
        tk.quit()
    if myX < 30  :
        myForwardX=1
    if myY < 30 :
        myForwardY=1
    canvas.coords(spritHandle, myX+myForwardX*3, myY +myForwardY*3)
    

    tk.update()
    
    canvas.after(10,moveIt)
moveIt()

tk.mainloop()