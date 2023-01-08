import turtle

PLAYER_1_START = (350, 0)
PLAYER_2_START = (-350, 0)
UP = 90
MOVE_SPEED = 20

class Paddle(turtle.Turtle):
    def __init__(self, team):
        super().__init__()
        self.penup()
        self.team = team
        self.setpos(PLAYER_1_START if self.team == 'player_1' else PLAYER_2_START)
        self.speed(10)
        self.setheading(UP)
        self.shape('square')
        self.turtlesize(1, 5)
        self.color('white')

    def go_up(self):
        if self.ycor() < 250:
            self.fd(MOVE_SPEED)

    def go_down(self):
        if self.ycor() > -250:
            self.bk(MOVE_SPEED)
