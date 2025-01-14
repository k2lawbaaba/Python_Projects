from turtle import Screen, Turtle
from pongSlate import PongSlate
from ball import Ball
import time
from scoreboard import Scoreboard

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 40
PADDLE_HEIGHT = 100
BALL_RADIUS = 10
PADDLE_COLLISION_BUFFER = 1290  # Adjust for paddle collision accuracy

# Screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# Draw the center partition
def draw_center_partition():
    ycor = -282
    for _ in range(30):
        partition = Turtle("square")
        partition.color("white")
        partition.shapesize(stretch_wid=0.5, stretch_len=0.1)
        partition.penup()
        partition.goto(0, ycor)
        ycor += 20

draw_center_partition()

# Create players and ball
r_player = PongSlate(SCREEN_WIDTH // 2 - PADDLE_WIDTH)
l_player = PongSlate(-SCREEN_WIDTH // 2 + PADDLE_WIDTH)
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()

# Paddle movement bindings
screen.onkey(r_player.up, "Up")
screen.onkey(r_player.down, "Down")
screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")

# Check for collision with paddles
def is_collision_with_paddle(ball, paddle):
    return (
        paddle.xcor() - PADDLE_WIDTH / 2 < ball.xcor() < paddle.xcor() + PADDLE_WIDTH / 2
        and paddle.ycor() - PADDLE_HEIGHT / 2 - BALL_RADIUS < ball.ycor() < paddle.ycor() + PADDLE_HEIGHT / 2 + BALL_RADIUS
    )

# Main game loop
game_is_on = True


while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Bounce ball on top and bottom walls
    if ball.ycor() > SCREEN_HEIGHT // 2 - BALL_RADIUS or ball.ycor() < -SCREEN_HEIGHT // 2 + BALL_RADIUS:
        ball.bounce_ball_y()

    # Detect collision with paddles
    if is_collision_with_paddle(ball, r_player) and ball.xcor() > SCREEN_WIDTH // 2 - PADDLE_COLLISION_BUFFER:
        ball.bounce_ball_x()
    elif is_collision_with_paddle(ball, l_player) and ball.xcor() < -SCREEN_WIDTH // 2 + PADDLE_COLLISION_BUFFER:
        ball.bounce_ball_x()

    # Ball out of bounds
    if ball.xcor() > SCREEN_WIDTH // 2:
        ball.reset_ball()
        scoreboard.l_player_score()

    elif ball.xcor() < -SCREEN_WIDTH // 2:
        ball.reset_ball()
        scoreboard.r_player_score()



screen.exitonclick()


