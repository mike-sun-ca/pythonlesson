import turtle as t

for i in range(30):
    t.pu()
    t.home()
    t.left(i*360/30)
    t.fd(100)
    t.left(135)
    t.speed(i)
    t.pd()
    t.fd(141)
    t.left(90)
    t.fd(141)
    t.left(90)
    t.fd(141)
    t.left(90)
    t.fd(141)
    
t.done()