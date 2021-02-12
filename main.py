import food
import snake
import map
import time
import score
import turtle


def set_easy():
    main_snake.pass_the_edge = True
    main_snake.eating_yourself_causes_death = False
    main_snake.having_wall = False
    main_map.set_difficulty('easy')


def set_normal():
    main_snake.pass_the_edge = True
    main_snake.eating_yourself_causes_death = True
    main_snake.having_wall = False
    main_map.set_difficulty('normal')


def set_hard():
    main_snake.pass_the_edge = False
    main_snake.eating_yourself_causes_death = True
    main_snake.having_wall = True
    main_map.set_difficulty('hard')


def set_asgar_mode():
    set_easy()
    food.Food.ASGAR_MODE = True
    main_snake.points.update_score()


def initializer(base_map):
    init = turtle.Turtle()
    init.penup()
    init.hideturtle()
    init.color('white')
    init.goto(0, 200)
    init.write('welcome to the snake game', False, 'center', ('Arial', 20, 'normal'))
    init.goto(-100, 100)
    init.write('1.easy', False, 'left', ('Arial', 15, 'normal'))
    init.goto(-100, 50)
    init.write('2.normal', False, 'left', ('Arial', 15, 'normal'))
    init.goto(-100, 0)
    init.write('3.hard', False, 'left', ('Arial', 15, 'normal'))
    base_map.screen.onkeypress(set_easy, '1')
    base_map.screen.onkeypress(set_normal, '2')
    base_map.screen.onkeypress(set_hard, '3')
    base_map.screen.onkeypress(set_asgar_mode, '4')
    return init


def start():
    # main_map.screen.reset()
    ini.clear()
    while not main_snake.gameOver:
        main_map.screen.update()
        main_snake.run()
        time.sleep(main_snake.delay)

    game_over = turtle.Turtle()
    game_over.penup()
    game_over.color('red')
    game_over.write('GAME OVER!', False, 'center', ('Arial', 20, 'normal'))
    time.sleep(5)
    game_over.clear()


main_map = map.Map()
main_map.screen.listen()
main_map.screen.setup(width=600, height=600)
main_snake = snake.Snake()
ini = initializer(main_map)
main_map.screen.onkeypress(start, 'space')


main_map.screen.onkeypress(main_snake.turn_right, 'Right')
main_map.screen.onkeypress(main_snake.turn_left, 'Left')
main_map.screen.onkeypress(main_snake.turn_up, 'Up')
main_map.screen.onkeypress(main_snake.turn_down, 'Down')



main_map.screen.exitonclick()
