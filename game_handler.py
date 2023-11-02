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
        self.angle = 90
        self.headings = {
            "east": 0,
            "north": 90,
            "west": 180,
            "south": 270
        }
        self.opposite_headings = {
            "east": "west",
            "north": "south",
            "west": "east",
            "south": "north"
        }

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

    def move_character(self, character):
        """
            Moves exactly one character, each time this function is called.
        """

    def move_all_characters_but_first(self, start_backwards=True):
        """
            Moves all characters in the status handler's character_list,
            into direction of the next character's position.
            By default the list is worked last to first.
            Set start_backwards to false, to reverse the movement order.
        """
        if start_backwards:
            range_steps = -1
        else:
            range_steps = 1

        for index in range(len(self.character_list)-1, 0, range_steps):
            next_position = self.character_list[index-1].pos()
            self.character_list[index].setpos(next_position)

    def move_first_character(self):
        """
            Moves only the first character in the character_list.
        """
        self.character_list[0].forward(self.character_pace)

    def turn_first_character_clockwise(self,):
        """
            Changes only the first characters heading clockwise.
        """
        self.character_list[0].right(self.angle)

    def turn_first_character_counter_clockwise(self):
        """
            Changes only the first characters heading clockwise.
        """
        self.character_list[0].left(self.angle)

    def turn_first_character_up(self):
        """
            Changes only the first characters heading upwards.
        """
        if self.character_list[0].heading() != self.headings["north"] \
                and self.character_list[0].heading() != self.headings["south"]:
            self.character_list[0].setheading(self.headings["north"])

    def turn_first_character_down(self):
        """
            Changes only the first characters heading downwards.
        """
        if self.character_list[0].heading() != self.headings["south"] \
                and self.character_list[0].heading() != self.headings["north"]:
            self.character_list[0].setheading(self.headings["south"])

    def turn_first_character_left(self):
        """
            Changes only the first characters heading left.
        """
        if self.character_list[0].heading() != self.headings["west"] \
                and self.character_list[0].heading() != self.headings["east"]:
            self.character_list[0].setheading(self.headings["west"])

    def turn_first_character_right(self):
        """
            Changes only the first characters heading right.
        """
        if self.character_list[0].heading() != self.headings["east"] \
                and self.character_list[0].heading() != self.headings["west"]:
            self.character_list[0].setheading(self.headings["east"])
