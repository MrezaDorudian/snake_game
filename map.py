from turtle import Screen, Turtle, colormode


class Map:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.tracer(0)


    def make_wall(self):
        turtle = Turtle('square')
        colormode(255)
        turtle.penup()
        turtle.color((150, 150, 150))
        turtle.goto(-300, -300)
        turtle.pensize(60)
        turtle.pendown()
        turtle.goto(-300, 300)
        turtle.goto(300, 300)
        turtle.goto(300, -300)
        turtle.goto(-300, -300)

        turtle.hideturtle()

    def set_difficulty(self, level):
        if level == 'hard':
            self.make_wall()
    pass
