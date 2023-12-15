from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Helvetica', 40, 'bold')
Y_POS = 240
X_POS = 35
score1 = Turtle()
score2 = Turtle()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.l_score()
        self.r_score()

    def l_score(self):
        score1.reset()
        score1.hideturtle()
        score1.penup()
        score1.pencolor("black")
        score1.color("white")
        score1.goto(x=-X_POS, y=Y_POS)
        score1.write(self.lscore, move=True, align=ALIGNMENT, font=FONT)

    def r_score(self):
        score2.reset()
        score2.hideturtle()
        score2.penup()
        score2.pencolor("black")
        score2.color("white")
        score2.goto(x=X_POS, y=Y_POS)
        score2.write(self.rscore, move=True, align=ALIGNMENT, font=FONT)

    def seperator(self):
        # sep.penup()
        self.screen.tracer(0)
        self.goto(0, -300)
        self.pendown()
        for _ in range(35):
            self.setheading(90)
            self.pensize(5)
            self.color("white")
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(15)

    def refresh(self):
        self.l_score()
        self.r_score()
