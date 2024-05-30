from turtle import Turtle

SCORE_LOCATION = (0, 270)
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"
SCORE_DISPLAY_COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor(SCORE_DISPLAY_COLOR)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(SCORE_LOCATION)
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def increment_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
