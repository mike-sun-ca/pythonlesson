#testGameMove


from ctypes import alignment
from email import message
import time
from tkinter import *
from tkinter import messagebox
from turtle import left, title
from tkinter import simpledialog
from numpy import record


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

canvas =Canvas(tk, width=500, height=450, bg="gray")
canvas.grid(row=1, column=0, columnspan=8)

meSquareHandle=canvas.create_rectangle(200,430,300, 460, fill="black")
robotImage=PhotoImage(file="robotspace50.gif")
spritHandle= canvas.create_image(250,100,image=robotImage)
scoreText=StringVar()
scoreText.set("Your score:")
myLabel = Label(tk, textvariable=scoreText, width=20).grid(row=0, column=0)

btn= Button(tk,text="exit", command=tk.quit, width=10).grid(row=0, column=7)



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
        handlerOfFile=open('record.log','a+')
        #handlerOfFile.close()
        #handlerOfFile=open('record.log','r+')
        handlerOfFile.seek(0)
        #        recordTxt1=handlerOfFile.read()
        recordTxt1="Score Leaderboard"
        recordListName=[]
        recordListScore=[]
        for i in range(10):
            
            recordTxt2 = handlerOfFile.readline() 
            
            #print("txt="+recordTxt1)
            #messagebox.showinfo(title= str(i), message=recordTxt1) 
            if not recordTxt2:
                print("pass")
                break
                pass
            else:
                recordTxt1=recordTxt1+ "\n "+ recordTxt2 
                recordTempName,recordTempScore=(recordTxt2.split(",",1))

                print("i="+str(i))
                print("txtName="+recordTempName)
                print("txtScore="+recordTempScore)
                #messagebox.showinfo(title= i, message=recordTxt1) 
        #if messagebox.askretrycancel(title="VanLan Game Class", message=recordTxt1) :
        if messagebox.askretrycancel(title="VanLan Game Class", message=recordTxt1+"\nGame over!! Do you want rety? or click cancle to exit") :
            #tk.title(recordTxt)
            myUserName1=simpledialog.askstring("Game Center","Please type your name here")
            if len(myUserName1) < 1 :
                myUserName1="Unknow User"
            handlerOfFile.write('\n'+myUserName1+" , "+str(myScore))
            handlerOfFile.close()
            myForwardX=1
            myForwardY=1
            myScore=0
            scoreText.set("Your score: "+ str(myScore))
            canvas.coords(spritHandle, 250, 100)
            myX=250
            myY=100
        else:
            handlerOfFile.close()
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