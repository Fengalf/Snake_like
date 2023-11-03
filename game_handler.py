import random
import turtle


class GameStatusHandler():
    def __init__(self) -> None:
        self.speed = 1
        self.score = 0
        self.point_size = 15
        self.point_random_location = (0, 0)
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
        self.character_list = []
        self.characters_at_start = 3
        self.refresh_rate = 0.1
        self.text_color = 'white'
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

    def is_going_on(self) -> bool:
        if self.character_list[0].pos()[0] <= (self.window_width)/2*-1 or self.character_list[0].pos()[0] >= (self.window_width)/2:
            return False
        elif self.character_list[0].pos()[1] <= (self.window_height)/2*-1 or self.character_list[0].pos()[1] >= (self.window_height)/2:
            return False
        elif self.character_colides_itself():
            return False
        return True

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

    def create_character(self, point_creation=False, scoreboard_creation=False):
        self.character = turtle.Turtle()
        self.character.penup()
        self.character.color(self.character_color)
        self.character.shape(self.character_shape)
        self.character.turtlesize(
            stretch_wid=self.character_size, stretch_len=self.character_size)
        self.character.speed(self.character_pace)
        if point_creation:
            self.character.setpos(self.point_random_location)
            return self.character
        elif scoreboard_creation:
            self.character.hideturtle()
            self.character.penup()
            self.character.sety(self.window_height/2-25)
            self.character.color(self.text_color)
            self.character.write(f"Score: {self.score}")
            return self.character
        else:
            self.character_list.append(self.character)

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

    def turn_first_character_clockwise(self):
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

    def create_random_point_cord_on_map(self):
        self.create_rand_x_coord()
        self.create_rand_y_coord()
        self.point_random_location = (self.rand_x_coord, self.rand_y_coord)

    def is_coord_reached(self) -> bool:
        """
            Checks if a range of coordinates are reached,
            \nusing `point_cord` as center.
        """
        x_snake, y_snake = self.character_list[0].pos()
        x_point, y_point = self.point_random_location

        x_point_min = x_point - self.point_size
        x_point_max = x_point + self.point_size
        y_point_min = y_point - self.point_size
        y_point_max = y_point + self.point_size

        return (x_point_min <= x_snake <= x_point_max) and (y_point_min <= y_snake <= y_point_max)

    def move_point(self, character):
        character.hideturtle()
        self.create_random_point_cord_on_map()
        character.setposition(self.point_random_location)
        character.showturtle()

    def add_character_to_list(self):
        """
            Creates another character that's at the end of the character_list
        """
        last_character_position: tuple = self.character_list[len(
            self.character_list)-1].pos()
        self.create_character()
        self.character_list[len(self.character_list)-1].setposition(
            last_character_position)

    def update_score(self, character):
        character.undo()
        character.write(f"Score: {self.score}")

    def character_colides_itself(self):
        first_char = self.character_list[0]
        first_char_pos = first_char.pos()
        first_char_x_pos, first_char_y_pos = first_char_pos
        for index in range(len(self.character_list)-1, 0, -1):
            current_char = self.character_list[index]
            current_char_pos = current_char.pos()
            current_char_x_pos, current_char_y_pos = current_char_pos

            current_char_min_x = current_char_x_pos - (self.point_size/3)
            current_char_max_x = current_char_x_pos + (self.point_size/3)
            current_char_min_y = current_char_y_pos - (self.point_size/3)
            current_char_max_y = current_char_y_pos + (self.point_size/3)

            if (current_char_min_x >= first_char_x_pos <= current_char_max_x) and (current_char_min_y >= first_char_y_pos <= current_char_max_y):
                return True
        return False
