import turtle as t
#circle background
t.fillcolor("gray")
t.begin_fill()
t.circle(100,360,200)
t.end_fill()
t.left(90)
t.pu()
t.fd(100)
t.right(90)
t.pd()
#draw a triangle bye for loop and fill different color      
for j in ("red","yellow","blue"):
    #every side and corner
    t.fillcolor(j)
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.left(120)
    t.left(120)
    t.end_fill()

t.done()

