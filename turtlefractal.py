import turtle

line = 50
for x in range(25):
	if x % 5 ==0:
		line += 20 
	turtle.forward(line)
	turtle.right(144)
turtle.exitonclick()
