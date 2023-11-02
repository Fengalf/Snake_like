# TODO Setup snake length
# TODO Setup snake growth
# TODO Setup snake speed increase
from turtle import Screen, Turtle
from game_handler import GameStatusHandler
import time


def is_coord_reached(snake_coord: tuple, point_coord: tuple, tolerance: int) -> bool:
    """
        Checks if a range of coordinates are reached,
        \nusing `point_cord` as center.
    """
    x_snake, y_snake = snake_coord
    x_point, y_point = point_coord

    x_point_min = x_point - tolerance
    x_point_max = x_point + tolerance
    y_point_min = y_point - tolerance
    y_point_max = y_point + tolerance

    return (x_point_min <= x_snake <= x_point_max) and (y_point_min <= y_snake <= y_point_max)


def snake_game():
    generate_new_point = True

    # Setting up the game handler
    game = GameStatusHandler()

    # Setting up the screen properties
    screen = Screen()
    screen.setup(width=game.window_width, height=game.window_height)
    screen.bgcolor(game.window_color)
    screen.tracer(0)
    screen.listen()

    # Our actual snake that we control
    snake_count = 3

    off_set = 0
    snakes = []
    for _ in range(0, snake_count):
        game.create_character()

    for snake in game.character_list:
        snake.setx(off_set)
        off_set -= 20

    game_is_on = True
    # game.refresh_rate = 0.75

    # Setting up the controls
    screen.onkey(key="Up", fun=game.turn_first_character_up)
    screen.onkey(key="Down", fun=game.turn_first_character_down)
    screen.onkey(key="Left", fun=game.turn_first_character_left)
    screen.onkey(key="Right", fun=game.turn_first_character_right)

    while game_is_on:
        screen.update()
        time.sleep(game.refresh_rate)

        game.move_all_characters_but_first()
        game.move_first_character()

    # # Setting up the points to collect as snake
    # points = Turtle()
    # points.shape('classic')
    # points.color('white')
    # points.penup()
    # points.hideturtle()

    # # Setting up the scoreboard
    # score_board = Turtle()
    # score_board.hideturtle()
    # score_board.penup()
    # score_board.sety(game.window_height/2-25)
    # score_board.color(game.text_color)
    # score_board.write(f"Score: {game.score}")

    # # Setting up the controls
    # screen.onkey(key="Up", fun=snake_moves.face_up)
    # screen.onkey(key="Down", fun=snake_moves.face_down)
    # screen.onkey(key="Left", fun=snake_moves.face_left)
    # screen.onkey(key="Right", fun=snake_moves.face_right)

    # while game.is_going_on([snakes[0].xcor(), snakes[0].ycor()]):
    #     screen.update()
    #     time.sleep(game.refresh_rate)
    #     # checking if a new point has to be generated
    #     if generate_new_point:
    #         generate_new_point = False
    #         game.create_rand_x_coord()
    #         game.create_rand_y_coord()

    #         # printing the dot / point
    #         points.setx(game.rand_x_coord)
    #         points.sety(game.rand_y_coord)
    #         points.dot(game.point_size)

    #     # moving the snake into heading direction
    #     for snake_index in range(len(snakes)-1, 0, -1):
    #         next_snake_position = snakes[snake_index-1].position()
    #         snakes[snake_index].goto(next_snake_position)
    #     snakes[0].forward(game.character_pace)

    #     # snapshotting the coordinations and putting them into a tuple
    #     snake_coord = (snakes[0].xcor(), snakes[0].ycor())
    #     random_coord = (game.rand_x_coord, game.rand_y_coord)

    #     # checking if a point was collected
    #     if is_coord_reached(snake_coord, random_coord, game.point_size):
    #         generate_new_point = True
    #         game.increase_score()
    #         score_board.undo()
    #         score_board.write(f"Score: {game.score}")
    #         points.clear()
    #         coords_of_last_snake = snakes[len(snakes)-1].position()
    #         new_snake = Turtle()
    #         new_snake.penup()
    #         new_snake.color(game.character_color)
    #         new_snake.shape(game.character_shape)
    #         new_snake.speed(game.speed)
    #         new_snake.width(game.character_size)
    #         new_snake.goto(coords_of_last_snake)
    #         snakes.append(snake)

    # game_over = Turtle(visible=False)
    # game_over.color(game.text_color)
    # game_over.write("Game Over.")
    screen.exitonclick()


if __name__ == "__main__":
    snake_game()
