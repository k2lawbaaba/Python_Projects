from turtle import Turtle
FONT=('arial', 30, 'normal')
ALIGN='center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.r_player=0
        self.l_player=0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.teleport(50, 240)
        self.write(self.r_player, align=ALIGN, font=FONT)
        self.teleport(-50, 240)
        self.write(self.l_player, align=ALIGN, font=FONT)

    def r_player_score(self):
        self.r_player +=1
        self.update_scores()
    def l_player_score(self):
        self.l_player +=1
        self.update_scores()
