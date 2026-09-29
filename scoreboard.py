from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
X_CORD = 0
Y_CORD = 270

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(X_CORD, Y_CORD)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.update_scorebaord()

    def update_scorebaord(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score+= 1
        self.clear()
        self.update_scorebaord()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scorebaord()

