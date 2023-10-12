import random
import turtle


class GameStatusHandler():
    def __init__(self) -> None:
        self.speed = 1
        self.score = 0
        self.point_size = 15
        self.window_color = 'black'
        self.window_width = 500
        self.window_height = 500
        self.rand_x_coord = 0
        self.rand_y_coord = 0
        self.threshold = self.score + 5
        self.character_size = 1
        self.character_shape = 'square'
        self.character_color = 'white'
        self.character_pace = 20
        self.refresh_rate = 0.1
        self.text_color = 'white'
        self.character_list = []
        self.characters_at_start = 3

    def level_up_speed(self):
        if self.score == self.threshold:
            self.threshold += 5
            self.speed += 1

    def increase_score(self):
        self.score += 1

    def is_going_on(self, character_pos: list) -> bool:
        if character_pos[0] <= (self.window_width)/2*-1 or character_pos[0] >= (self.window_width)/2:
            return False
        elif character_pos[1] <= (self.window_height)/2*-1 or character_pos[1] >= (self.window_height)/2:
            return False
        return True

    def create_rand_x_coord(self) -> int:
        self.coord = random.randint(
            self.window_width/2*-1, self.window_width/2)
        self.rand_x_coord = self.rand_cord_checker(
            self.coord, self.window_width)

    def create_rand_y_coord(self) -> int:
        self.coord = random.randint(
            self.window_height/2*-1, self.window_height/2)
        self.rand_y_coord = self.rand_cord_checker(
            self.coord, self.window_height)

    def rand_cord_checker(self, coord, screen_axis) -> int:
        if coord >= (screen_axis/2) - self.point_size - 1:
            return int(coord - self.point_size)
        elif coord <= (screen_axis/2*-1) + self.point_size + 1:
            return int(coord + self.point_size)
        return int(coord)

    def create_character(self):
        self.character = turtle.Turtle()
        self.character.penup()
        self.character.color(self.character_color)
        self.character.shape(self.character_shape)
        self.character.turtlesize(
            stretch_wid=self.character_size, stretch_len=self.character_size)
        self.character.speed(self.character_pace)
        self.character_list.append(self.character)
