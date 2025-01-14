import turtle as t
import turtle_maker as tm
import random

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]
def movement_turtle(turtle, x_axis, y_axis, colour):
    turtle.color(colour)
    turtle.pu()
    turtle.goto(x=x_axis, y=y_axis)

def move_forward(turtle, distance):
     turtle.fd(distance)

# n=tm.TurtleMaker()
turtles=[]
is_race_on=False
screen = t.Screen()
screen.title("Turtle Race")
screen.setup(width=700, height=400)
y_axis=[-80,-40,0,40,80,120]

for x in range(0,6):
    created_turtle=t.Turtle(shape="turtle")
    movement_turtle(turtle=created_turtle, x_axis=-230, y_axis=y_axis[x], colour=colors[x])
    turtles.append(created_turtle)

user_input= screen.textinput(title="Make your stand", prompt="Place your odd")

if user_input:
    is_race_on= True

while is_race_on:
    for x in turtles:

        if x.xcor() > 220:
            if x.pencolor() == user_input:
                x.write(f"Congratulations, Turtle {x.pencolor().upper()} won the race", True, align="center")
            else:
                x.write(f"Sorry, Turtle {x.pencolor().upper()} won the race", True, align="center")
            is_race_on = False
        rand_dist = random.randint(0, 10)
        move_forward(x, rand_dist)
        # print(round(x.xcor()), x.pencolor())

screen.exitonclick()
