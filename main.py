# TODO Change from one Game handler class to multiple classes: 1. Snake, 2. Points, 3. Scoreboard
# TODO Alternatively go with how it is and make points vanish as soon as they're reached
# TODO Setup snake speed increase every x points

from snake_handler import SnakeController
from food_handler import FoodController
from score_handler import ScoreController
from turtle import Screen
import time


def snake_game():
    # Setting up the game controllers
    snake_character = SnakeController()
    food = FoodController()
    scoreboard = ScoreController()
    screen = Screen()

    # Setting variables used
    width = 500
    height = 500

    # setting up the screen
    screen.setup(width=width,
                 height=height)
    screen.bgcolor('black')
    screen.tracer(0)
    screen.listen()

    for _ in range(0, snake_character.characters_at_start):
        snake_character.create_segment()

    off_set = 0
    for snake in snake_character.segment_list:
        snake.setx(off_set)
        off_set -= 20

    # Setting up the input controls
    screen.onkey(key="Up", fun=snake_character.turn_first_character_up)
    screen.onkey(key="Down", fun=snake_character.turn_first_character_down)
    screen.onkey(key="Left", fun=snake_character.turn_first_character_left)
    screen.onkey(key="Right", fun=snake_character.turn_first_character_right)

    # create the first food
    food.create_random_point_cord_on_map()
    food.move_point()

    # running the game itself
    while snake_character.is_going_on():
        screen.update()
        time.sleep(scoreboard.refresh_rate)

        snake_character.move_all_characters_but_first()
        snake_character.move_first_character()

        if int(food.distance(snake_character.segment_list[0].pos())) <= food.point_size:
            food.move_point()
            snake_character.add_character_to_list()
            scoreboard.refresh_score()

    scoreboard.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    snake_game()
