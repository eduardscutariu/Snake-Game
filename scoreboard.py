from turtle import Turtle
ALIGNEMENT = 'center'
FONT = ('Courier', 24, 'normal')
class ScoreB(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"score: {self.score}", move=False, align=ALIGNEMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", move=False, align=ALIGNEMENT, font=FONT)

    #def game_over(self):
        #self.clear()
        #self.goto(0,0)
        #self.write(f"game over", move=False, align=ALIGNEMENT, font=FONT)
    def reset(self):
        if self.high_score > self.score:
            self.high_score = self.score
        self.score = 0

