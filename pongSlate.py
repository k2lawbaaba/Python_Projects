from turtle import Turtle
UP=90
DOWN=270
class PongSlate(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.fillcolor("white")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.teleport(position,0)
        self.speed("fastest")

    def up(self):
        if self.ycor()<258:
            new_ycor= self.ycor() + 30
            self.goto(self.xcor(),new_ycor)

    def down(self):
        if self.ycor() > -240:
            new_ycor = self.ycor() - 30
            self.goto(self.xcor(), new_ycor)


    def move_slate(self,position):
        self.teleport(position, 0)



