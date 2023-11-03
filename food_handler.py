from turtle import Turtle
import random


class FoodController(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.window_width = 500
        self.window_height = 500
        self.point_size = 15

    def create_rand_x_coord(self) -> int:
        self.coord = random.randint(
            int(self.window_width/2*-1), int(self.window_width/2))
        self.rand_x_coord = self.rand_cord_checker(
            self.coord, self.window_width)

    def create_rand_y_coord(self) -> int:
        self.coord = random.randint(
            int(self.window_height/2*-1), int(self.window_height/2))
        self.rand_y_coord = self.rand_cord_checker(
            self.coord, self.window_height)

    def rand_cord_checker(self, coord, screen_axis) -> int:
        if coord >= (screen_axis/2) - self.point_size - 1:
            return int(coord - self.point_size)
        elif coord <= (screen_axis/2*-1) + self.point_size + 1:
            return int(coord + self.point_size)
        return int(coord)

    def create_random_point_cord_on_map(self):
        self.create_rand_x_coord()
        self.create_rand_y_coord()
        self.point_random_location = (self.rand_x_coord, self.rand_y_coord)

    def is_coord_reached(self, segment: Turtle) -> bool:
        """
            Checks if a range of coordinates are reached,
            \nusing `point_cord` as center.
        """
        x_snake, y_snake = segment.pos()
        x_point, y_point = self.point_random_location

        x_point_min = x_point - self.point_size
        x_point_max = x_point + self.point_size
        y_point_min = y_point - self.point_size
        y_point_max = y_point + self.point_size

        return (x_point_min <= x_snake <= x_point_max) and (y_point_min <= y_snake <= y_point_max)

    def move_point(self):
        self.create_random_point_cord_on_map()
        self.setposition(self.point_random_location)
