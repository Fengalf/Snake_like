import random
import turtle


class SnakeController():
    def __init__(self) -> None:
        self.speed = 1
        self.window_color = 'black'
        self.window_width = 500
        self.window_height = 500
        self.character_size = 1
        self.character_shape = 'square'
        self.character_color = 'white'
        self.character_pace = 20
        self.segment_list = []
        self.characters_at_start = 3
        self.headings = {
            "east": 0,
            "north": 90,
            "west": 180,
            "south": 270
        }

    def level_up_speed(self):
        if self.score == self.threshold:
            self.threshold += 5
            self.speed += 1

    def is_going_on(self) -> bool:
        if self.segment_list[0].pos()[0] <= (self.window_width)/2*-1 or self.segment_list[0].pos()[0] >= (self.window_width)/2:
            return False
        elif self.segment_list[0].pos()[1] <= (self.window_height)/2*-1 or self.segment_list[0].pos()[1] >= (self.window_height)/2:
            return False
        elif self.character_colides_itself():
            return False
        return True

    def create_segment(self):
        """
            Creates a segment and appends it to the segment_list
        """
        self.segment = turtle.Turtle()
        self.segment.penup()
        self.segment.color(self.character_color)
        self.segment.shape(self.character_shape)
        self.segment.turtlesize(
            stretch_wid=self.character_size, stretch_len=self.character_size)
        self.segment.speed(self.character_pace)
        self.segment_list.append(self.segment)

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

        for index in range(len(self.segment_list)-1, 0, range_steps):
            next_position = self.segment_list[index-1].pos()
            self.segment_list[index].setpos(next_position)

    def move_first_character(self):
        """
            Moves only the first character in the character_list.
        """
        self.segment_list[0].forward(self.character_pace)

    def turn_first_character_up(self):
        """
            Changes only the first characters heading upwards.
        """
        if self.segment_list[0].heading() != self.headings["south"]:
            self.segment_list[0].setheading(self.headings["north"])

    def turn_first_character_down(self):
        """
            Changes only the first characters heading downwards.
        """
        if self.segment_list[0].heading() != self.headings["north"]:
            self.segment_list[0].setheading(self.headings["south"])

    def turn_first_character_left(self):
        """
            Changes only the first characters heading left.
        """
        if self.segment_list[0].heading() != self.headings["east"]:
            self.segment_list[0].setheading(self.headings["west"])

    def turn_first_character_right(self):
        """
            Changes only the first characters heading right.
        """
        if self.segment_list[0].heading() != self.headings["west"]:
            self.segment_list[0].setheading(self.headings["east"])

    def add_character_to_list(self):
        """
            Creates another character that's at the end of the character_list
        """
        last_character_position: tuple = self.segment_list[-1].pos()
        self.create_segment()
        self.segment_list[-1].setposition(last_character_position)

    def character_colides_itself(self):
        """
            Checks if the first segment colides with it's trailing segments.
        """
        first_char = self.segment_list[0]
        for segment in self.segment_list[1:]:
            if first_char.distance(segment) <= self.character_size:
                return True
        return False
