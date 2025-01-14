class TurtleMaker:

    def __init__(self, shape):
        self.name = "red"
        self.shape=shape
        self.color="red"
    def make_turtle(self, turtle):
         name= turtle.Turtle(self.shape)
         name.color=self.color
         return name

    def movements(self,name_turtle):
        name_turtle.pu()
        name_turtle.goto(x=-240, y=0)
    # def move_forward(self,turtle, distance):
    #         turtle.fd(distance)
