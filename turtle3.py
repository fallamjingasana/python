import turtle

my_win = turtle.Screen()
my_win.bgcolor("green")
my_win.title("'turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size =size-5
    size = size + 1