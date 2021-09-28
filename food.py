from turtle import *
from random import randint
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("HotPink")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.speed(10)
        self.penup()
        self.refresh()
    

    def refresh(self):
        range_x = randint(-280,280)
        range_y = randint(-280,280)
        self.goto(range_x, range_y)