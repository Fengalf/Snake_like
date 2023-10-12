from turtle import Turtle


class MoveTurtle:
    def __init__(self, turtle: Turtle, distance: int = 10, angle: int = 10) -> None:
        self.turtle = turtle
        self.distance = distance
        self.angle = angle
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

    def heading_own_direction(self):
        self.turtle_direction: int = self.turtle.heading()
        self.headings_keys: list = self.headings.keys()
        self.headings_values: list = self.headings.values()
        self.turtle_cardinal_direction: str = self.headings_keys[self.headings_values.index(
            self.turtles_heading)]
        return self.turtle.heading() == self.headings[self.turtle_cardinal_direction]

    def heading_opposite_direction(self):
        self.turtle_direction: int = self.turtle.heading()
        self.headings_keys: list = self.headings.keys()
        self.headings_values: list = self.headings.values()
        self.turtle_cardinal_direction: str = self.headings_keys[self.headings_values.index(
            self.turtles_heading)]
        return self.turtle_cardinal_direction == self.opposite_headings[self.turtle_cardinal_direction]

    def up(self):
        if not self.heading_own_direction() and not self.heading_opposite_direction():
            self.turtle.setheading(self.headings["north"])
        self.turtle.forward(self.distance)

    def down(self):
        if not self.heading_own_direction() and not self.heading_opposite_direction():
            self.turtle.setheading(self.headings["south"])
        self.turtle.forward(self.distance)

    def left(self):
        if not self.heading_own_direction() and not self.heading_opposite_direction():
            self.turtle.setheading(self.headings["west"])
        self.turtle.forward(self.distance)

    def right(self):
        if not self.heading_own_direction() and not self.heading_opposite_direction():
            self.turtle.setheading(self.headings["east"])
        self.turtle.forward(self.distance)

    def face_up(self):
        if self.turtle.heading() != self.headings["north"]:
            self.turtle.setheading(self.headings["north"])

    def face_down(self):
        if self.turtle.heading() != self.headings["south"]:
            self.turtle.setheading(self.headings["south"])

    def face_left(self):
        if self.turtle.heading() != self.headings["west"]:
            self.turtle.setheading(self.headings["west"])

    def face_right(self):
        if self.turtle.heading() != self.headings["east"]:
            self.turtle.setheading(self.headings["east"])

    def forward(self):
        self.turtle.forward(self.distance)

    def backwards(self):
        self.turtle.backward(self.distance)

    def clockwise(self):
        self.turtle.right(self.angle)

    def counter_clockwise(self):
        self.turtle.left(self.angle)
