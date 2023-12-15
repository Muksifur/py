from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        """
        This takes tuple as an argument. the first item in the tuple should be the x position of the paddle and the
        second item should be the y position.
        """
        super().__init__()
        self.position = position
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(self.position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
