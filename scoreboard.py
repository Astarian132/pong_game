import turtle

PLAYER_1 = (150, 260)
PLAYER_2 = (-150, 260)

ALLIGNEMNT = "center"
FONT = ("Courier", 40, "bold")

class Scoreboard(turtle.Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.speed(10)
        self.penup()
        self.goto(PLAYER_1 if player == 'player_1' else PLAYER_2)
        self.score = 0
        self.color('white')

    def show_score(self):
        self.clear()
        self.write(self.score , False, align=ALLIGNEMNT, font=FONT)

    def goal(self):
        self.score += 1
        self.show_score()