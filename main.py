import turtle as t

tt= t.Turtle()
screen = t.Screen()
tt.speed(10)
def move_forward():
    tt.fd(10)
def move_around():
    tt.fd(5)
    tt.lt(5)

def move_clockwise():
    tt.lt(10)

def move_anti_clockwise():
    tt.rt(10)

def move_backward():
    tt.bk(10)
def clear_screen():
    tt.home()
    tt.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_clockwise, "d")
screen.onkey(move_anti_clockwise, "a")
screen.onkey(move_backward, "s")
screen.onkey(clear_screen, "c")
screen.onkey(move_around, "r")



screen.exitonclick()