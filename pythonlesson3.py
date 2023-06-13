import turtle as t
bowR=100
t.left(120)
for rainbowColor in ("red","orange","yellow","green","blue", "indigo", "violet"):
    t.fillcolor(rainbowColor)
    t.begin_fill()
    
    t.circle(bowR,120)
    t.right(90)
    t.fd(20)
    t.right(90)
    t.circle(-(bowR+20),120)
    t.right(90)
    t.fd(20)
    t.end_fill()

    t.pu()

    t.left(180)
    bowR+=20
    t.fd(20)
    t.left(90)
    t.pd()
t.done()

t.fillcolor("orange")
t.begin_fill()
t.left(90)
t.circle(120,120)
t.right(90)
t.fd(20)
t.right(90)
t.circle(-140,120)
t.right(90)
t.fd(20)
t.end_fill()
t.done()