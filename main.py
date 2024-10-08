import turtle 
t=turtle.Turtle()
scrn=turtle.Screen()
scrn.listen()

def forward():
    t.forward(10)
# forward()
def backward():
    t.backward(10)   
def right():
    t.right(10)
def left():
    t.left(10)     
def clear():
    t.reset()       
scrn.onkey(key="w",fun=forward)
scrn.onkey(key="s",fun=backward)
scrn.onkey(key="d",fun=right)
scrn.onkey(key="a",fun=left)
scrn.onkey(key="c",fun=clear)






















scrn.exitonclick()