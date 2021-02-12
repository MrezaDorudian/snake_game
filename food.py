from turtle import Turtle
import snake
import random


class Food:
    OLD_FOODS = []
    ASGAR_MODE = False

    def __init__(self, main_snake):
        coordinates = []

        for i in range(-280, 300, 20):
            for j in range(-280, 300, 20):
                if main_snake.having_wall:
                    if i == -280 or i == 280 or j == -280 or j == 280:
                        continue
                coordinates.append((i, j))

        to_pick = set(coordinates) - set(snake.Snake.coordinates)
        if Food.ASGAR_MODE:
            to_pick -= set(Food.OLD_FOODS)

        coord = random.choice(list(to_pick))
        self.x, self.y = coord
        Food.OLD_FOODS.append((self.x, self.y))

        self.food = Turtle('circle')
        self.food.shapesize(0.65, 0.65)
        self.food.color('yellow')
        self.food.penup()
        self.food.speed('fastest')
        self.food.goto(self.x, self.y)
        if Food.ASGAR_MODE:
            self.food.hideturtle()
            self.food.write('عسگر')

    pass
