#print star

import turtle


def draw_pentagram(size):

    # 计数器
    count = 1
    turtle.penup()
    turtle.backward(5)
    turtle.pendown()
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1


def main():
  
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    while size <= 100:
        # 调用函数
        draw_pentagram(size)
        # size = size + 10
        size += 10

    turtle.exitonclick()


if __name__ == '__main__':
    main()


