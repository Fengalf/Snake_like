# TODO Change from one Game handler class to multiple classes: 1. Snake, 2. Points, 3. Scoreboard
# TODO Alternatively go with how it is and make points vanish as soon as they're reached
# TODO Setup snake speed increase every x points

from turtle import Screen, Turtle
from snake_handler import SnakeController
from food_handler import FoodController
import time


def snake_game():
    generate_new_point = True

    # Setting up the game handlers
    snake_character = SnakeController()
    point = FoodController()
    score_board = snake_character.create_segment(scoreboard_creation=True)

    # Setting up the screen properties
    screen = Screen()
    screen.setup(width=snake_character.window_width,
                 height=snake_character.window_height)
    screen.bgcolor(snake_character.window_color)
    screen.tracer(0)
    screen.listen()

    # Our actual snake that we control
    snake_count = 3

    off_set = 0
    for _ in range(0, snake_character.characters_at_start):
        snake_character.create_segment()

    for snake in snake_character.segment_list:
        snake.setx(off_set)
        off_set -= 20

    # Setting up the controls
    screen.onkey(key="Up", fun=snake_character.turn_first_character_up)
    screen.onkey(key="Down", fun=snake_character.turn_first_character_down)
    screen.onkey(key="Left", fun=snake_character.turn_first_character_left)
    screen.onkey(key="Right", fun=snake_character.turn_first_character_right)

    point.create_random_point_cord_on_map()
    point.move_point()

    while snake_character.is_going_on():
        screen.update()
        time.sleep(snake_character.refresh_rate)

        snake_character.move_all_characters_but_first()
        snake_character.move_first_character()

        if point.is_coord_reached(segment=snake_character.segment_list[0]):
            point.move_point()
            snake_character.add_character_to_list()
            snake_character.score += 1
            snake_character.update_score(score_board)

    # game_over = Turtle(visible=False)
    # game_over.color(game.text_color)
    # game_over.write("Game Over.")
    screen.exitonclick()


if __name__ == "__main__":
    snake_game()
