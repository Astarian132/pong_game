import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(10)
        self.setpos(0, 0)
        self.x_move = 8
        self.y_move = 8
        self.ball_speed = 1
        self.shape('circle')
        self.color('white')

    def move(self):
        self.goto(self.xcor() + (self.ball_speed * self.x_move), self.ycor() + (self.ball_speed * self.y_move))
        self.detect_wall()

    def detect_wall(self):
        #detect wall
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_move *= -1

    def detect_paddle(self, paddle):
        # check detection
        if self.distance(paddle) < 50:
            self.x_move *= -1
            self.ball_speed *= 1.1
        # check if goal
        elif abs(self.xcor()) > 380:
            return False

    def reset_position(self):
        self.setpos(0,0)
        self.ball_speed = 1
        self.x_move *= -1








