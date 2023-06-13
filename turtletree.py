import turtle as tl 
def draw_smalltree(tree_length,tree_angle): 
    ''' 
    绘制分形树函数
    ''' 
    if tree_length >= 3:
        tl.pendown() 
        if tree_length <= 30: #树枝长小于30，可以当作树叶了，树叶部分为绿色 
            tl.pencolor('green') 
        else:
            tl.pencolor('brown') #树干部分为棕色 
         
        tl.right(tree_angle) #往右转 
        tl.forward(tree_length) #往前画
        draw_smalltree(tree_length - 10,tree_angle)#画下一枝，直到画到树枝长小于3 
        tl.penup()
        tl.backward(tree_length)
        tl.pendown()
        tl.left(2 * tree_angle) #转向画左 
        if tree_length <= 30: #树枝长小于30，可以当作树叶了，树叶部分为绿色 
            tl.pencolor('green') 
        else:
            tl.pencolor('brown') #树干部分为棕色 
        tl.forward(tree_length) #往前画 
        draw_smalltree(tree_length -10,tree_angle) #直到画到树枝长小于3 
        
        tl.penup()
        tl.backward(tree_length) #往回画，回溯到上一层 
        tl.pendown()
        tl.rt(tree_angle) #转到正向上的方向，然后回溯到上一层 

def main(): 
    tl.penup() 
    tl.pencolor('black') 
    tl.speed(9)
    tl.screensize(1200,600)
    tl.left(90) #因为树是往上的，所以先把方向转左 
    tl.backward(350) #把起点放到底部 
    
    tree_length = 120 #我设置的最长树干为100 
    tree_angle = 20 #树枝分叉角度，我设为20 
    draw_smalltree(tree_length,tree_angle) 
    tl.exitonclick() #点击才关闭画画窗口 
    
if __name__ == '__main__': 
    main()