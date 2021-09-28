from turtle import *
FONT = ('courier', 12)
ALIGNMENT = "center"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.setpos(0,280)
        self.hideturtle()
        self.color('white')
        self.score = 0
        with open('e:/Python/snake game/data.txt','r') as f:
            self.highscore = int(f.read())
        self.writescore()
        

    def writescore(self):
        self.clear()
        self.write(f"Socre: {self.score} High score: {self.highscore}" ,align = ALIGNMENT, font=FONT)

    def resetscore(self):
        with open('data.txt','r+') as f:
            if self.score > self.highscore:
                self.highscore = self.score
                f.write(str(self.highscore))
        self.score = 0
        self.writescore()

    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write("GAME OVER",font=FONT)

    def increase(self):
        self.score += 1
        self.writescore()

