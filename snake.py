import time
from turtle import Turtle
import score

import food


class Snake:

    SPEED = 20
    STARTING_LENGTH = 3
    STARTING_DIRECTION = 'right'
    xCoordinates = []
    yCoordinates = []
    coordinates = []

    def __init__(self):
        self.delay = 0.1
        self.gameOver = False
        self.points = score.ScoreBoard()
        self.pass_the_edge = False
        self.eating_yourself_causes_death = True
        self.having_wall = True
        self.body = []
        self.length = self.STARTING_LENGTH
        self.direction = self.STARTING_DIRECTION
        self.food = None
        self.make_snake()

    def make_snake(self):
        x = 0
        y = 0
        for i in range(self.length):
            temp_snake = Turtle('circle')
            temp_snake.color('white')
            temp_snake.penup()
            temp_snake.goto(x, y)
            Snake.xCoordinates.append(x)
            Snake.yCoordinates.append(y)
            Snake.coordinates.append((x, y))
            self.body.append(temp_snake)
            x -= self.SPEED
        self.food = food.Food(self)

    def turn_right(self):
        if self.direction != 'left' and self.direction != 'right':
            for i in range(len(self.body)):
                if i == 0:
                    self.body[i].setheading(0)
            self.direction = 'right'
            self.run()
            time.sleep(0.01)

    def turn_left(self):
        if self.direction != 'right' and self.direction != 'left':
            for i in range(len(self.body)):
                if i == 0:
                    self.body[i].setheading(180)
            self.direction = 'left'
            self.run()
            time.sleep(0.01)

    def turn_up(self):
        if self.direction != 'down' and self.direction != 'up':
            for i in range(len(self.body)):
                if i == 0:
                    self.body[i].setheading(90)
            self.direction = 'up'
            self.run()
            time.sleep(0.01)

    def turn_down(self):
        if self.direction != 'up' and self.direction != 'down':
            self.body[0].setheading(270)
            self.direction = 'down'
            self.run()
            time.sleep(0.01)

    def run(self):
        Snake.xCoordinates.clear()
        Snake.yCoordinates.clear()
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())
        self.body[0].forward(self.SPEED)

        if self.pass_the_edge:
            if self.body[0].xcor() >= 300:
                self.body[0].goto(-300, self.body[0].ycor())
            elif self.body[0].xcor() <= -300:
                self.body[0].goto(300, self.body[0].ycor())
            elif self.body[0].ycor() >= 300:
                self.body[0].goto(self.body[0].xcor(), -300)
            elif self.body[0].ycor() <= -300:
                self.body[0].goto(self.body[0].xcor(), 300)

        if self.eating_yourself_causes_death:
            for part in self.body[1:]:
                if self.body[0].distance(part) < 10:
                    self.gameOver = True

        for part in self.body:
            Snake.xCoordinates.append(part.xcor())
            Snake.yCoordinates.append(part.ycor())
            Snake.coordinates.append((part.xcor, part.ycor))


        # food eaten
        if round(self.body[0].xcor()) == self.food.x and round(self.body[0].ycor()) == self.food.y:
            self.points.your_score += 1
            self.points.update_score()
            self.food.food.hideturtle()
            self.delay -= (self.delay * 0.09)

            temp_snake = Turtle('square')
            temp_snake.color('white')
            temp_snake.speed('fastest')
            temp_snake.penup()
            last_index = len(Snake.xCoordinates) - 1
            temp_snake.goto(Snake.xCoordinates[last_index], Snake.yCoordinates[last_index])
            self.body.append(temp_snake)
            self.food = food.Food(self)

        if self.having_wall:
            if (round(self.body[0].xcor()) == 280) or (round(self.body[0].xcor()) == -280) or\
                    round(self.body[0].ycor()) == 280 or round(self.body[0].ycor()) == -280:
                self.gameOver = True

    pass
