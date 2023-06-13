import turtle as t
t.screensize(400,300)
t.reset()
t.setworldcoordinates(-100,-150,300,150)
t.color('red', 'yellow')
t.speed(0)
t.begin_fill()

while True:
    t.forward(200)
    t.left(170)
    print(abs(t.pos()))
    if abs(t.pos()) < 1:
        break
t.end_fill()
t.done()