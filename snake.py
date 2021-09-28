from turtle import *
MOVE_DISTANCE = 20
UP = 90  
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: 
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        self.n = 0
        for t in range(3):
            t = Turtle(shape = 'square')
            t.color('white')
            t.penup()
            t.setpos(self.n,0)
            self.n -= 20
            self.all_snakes.append(t)
    
    def add_snake(self,position):
            t = Turtle(shape = 'square')
            t.color('white')
            t.penup()
            t.setpos(position)
            self.all_snakes.append(t)

    def extend_snake(self):
        self.add_snake(self.all_snakes[-1].position())


    def move_snake(self):
        for t in range(len(self.all_snakes)-1, 0, -1):
            t_x = self.all_snakes[t-1].xcor()
            t_y = self.all_snakes[t-1].ycor()
            self.all_snakes[t].goto(t_x,t_y)
        self.head.forward(MOVE_DISTANCE)


    def reset_snake(self):
        for snake in self.all_snakes:
            snake.goto(1000,1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)
     
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)
