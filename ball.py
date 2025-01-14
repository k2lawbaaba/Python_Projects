from turtle import Turtle
import random
rand=random.randrange(10,30)
rand2=random.randrange(10,30)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_value = "fastest"
        self.ball_speed = 0.05
        self.recreate_ball()
        self.x_cor = rand
        self.y_cor = rand

    def recreate_ball(self):
        self.shape("circle")
        self.fillcolor("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.pu()
        self.speed(self.speed_value)
        self.x_cor = 10
        self.y_cor = 10


    def move_ball(self):
        xcor=self.xcor() + self.x_cor
        ycor=self.ycor() + self.y_cor
        self.goto(xcor, ycor)


    def bounce_ball_y(self):
        self.y_cor *= -1
    def reset_ball(self):
        # self.hideturtle()
        # if self.xcor() >0 and self.ycor() > 0:
        #     self.goto(-0,-0)
        #     self.x_cor *= -1
        #     self.y_cor *= -1
        # else:
        #     self.goto(0,0)
        #     self.x_cor = 10
        #     self.y_cor = 10
        # self.showturtle()
        self.home()
        self.ball_speed = 0.05
        self.x_cor *= -1
        # self.increase_speed()


    def bounce_ball_x(self):
        self.x_cor *= -1
        self.ball_speed *=0.8
    # def increase_speed(self):
    #     if 0 < self.speed_value and not self.speed_value >= 11:
    #         self.speed_value += self.starting_value
    #         self.starting_value +=1
    #     else:
    #         self.speed_value =0
