from turtle import Turtle

WIDTH = 20
HEIGHT = 20
X_POS = 0
Y_POS = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(X_POS, Y_POS)
        self.screen.update()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        if self.y_move > 0:
            self.y_move += 1
        elif self.y_move < 0:
            self.y_move -= 1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        if self.x_move > 0:
            self.x_move += 1
        elif self.x_move < 0:
            self.x_move -= 1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
