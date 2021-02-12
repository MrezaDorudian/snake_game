from turtle import Turtle

import food


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.your_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color('cyan')
        if food.Food.ASGAR_MODE:
            self.write(f'Score: {self.your_score}(congrats Hidden level)', False, 'center', ('Arial', 20, 'normal'))
        else:
            self.write(f'Score: {self.your_score}', False, 'center', ('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        if food.Food.ASGAR_MODE:
            self.write(f'Score: {self.your_score}(congrats Hidden level)', False, 'center', ('Arial', 20, 'normal'))
        else:
            self.write(f'Score: {self.your_score}', False, 'center', ('Arial', 20, 'normal'))



    pass
