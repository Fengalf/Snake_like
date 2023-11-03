# TODO Change from one Game handler class to multiple classes: 1. Snake, 2. Points, 3. Scoreboard
# TODO Alternatively go with how it is and make points vanish as soon as they're reached
# TODO Setup snake speed increase every x points

from turtle import Screen, Turtle
from game_handler import GameStatusHandler
import time


def snake_game():
    generate_new_point = True

    # Setting up the game handlers
    game = GameStatusHandler()
    point = game.create_character(point_creation=True)
    score_board = game.create_character(scoreboard_creation=True)

    # Setting up the screen properties
    screen = Screen()
    screen.setup(width=game.window_width, height=game.window_height)
    screen.bgcolor(game.window_color)
    screen.tracer(0)
    screen.listen()

    # Our actual snake that we control
    snake_count = 3

    off_set = 0
    for _ in range(0, game.characters_at_start):
        game.create_character()

    for snake in game.character_list:
        snake.setx(off_set)
        off_set -= 20

    # Setting up the controls
    screen.onkey(key="Up", fun=game.turn_first_character_up)
    screen.onkey(key="Down", fun=game.turn_first_character_down)
    screen.onkey(key="Left", fun=game.turn_first_character_left)
    screen.onkey(key="Right", fun=game.turn_first_character_right)

    game.create_random_point_cord_on_map()
    game.move_point(point)

    while game.is_going_on():
        screen.update()
        time.sleep(game.refresh_rate)

        game.move_all_characters_but_first()
        game.move_first_character()

        if game.is_coord_reached():
            game.move_point(point)
            game.add_character_to_list()
            game.score += 1
            game.update_score(score_board)

    # game_over = Turtle(visible=False)
    # game_over.color(game.text_color)
    # game_over.write("Game Over.")
    screen.exitonclick()


if __name__ == "__main__":
    snake_game()
