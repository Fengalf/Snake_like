from turtle import Turtle


class ScoreController(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        # setting own attributes
        self.width = 500
        self.height = 500
        self.score = 0
        self.refresh_rate = 0.1

        # setting up the scoreboard
        self.penup()
        self.hideturtle()
        self.penup()
        self.sety(self.height/2-25)
        self.color("white")
        self.speed("fastest")
        self.write(f"Score: {self.score}")

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over")

    def refresh_score(self):
        self.undo()
        self.score += 1
        self.write(f"Score: {self.score}")
