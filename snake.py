from turtle import Turtle


class Snake:
    TURTLE_WIDTH = 20
    INITIAL_LENGTH = 3

    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270

    def __init__(self):
        self.links = []
        self.create_snake()
        self.head = self.links[0]

    def create_snake(self):
        for index in range(Snake.INITIAL_LENGTH):
            position_x = -index * Snake.TURTLE_WIDTH
            new_link = Turtle("square")
            new_link.penup()
            new_link.color("white")
            new_link.goto(position_x, 0)
            self.links.append(new_link)

    def add_link(self):
        pos = self.links[- 1].position()
        new_link = Turtle("square")
        new_link.penup()
        new_link.color("white")
        new_link.goto(pos)
        self.links.append(new_link)

    def move(self):
        for index in range(len(self.links) - 1, 0, -1):
            self.links[index].goto(self.links[index-1].xcor(), self.links[index-1].ycor())

        self.head.forward(Snake.TURTLE_WIDTH)

    def right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)

    def up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)

    def down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def detect_collision_with_tail(self):
        for link in self.links[1:]:
            if self.head.distance(link) < 10:
                return True
        return False
            
    # def minimum_distance_from_screen(self):
    #     x, y = self.head.position()
    #     dis_from_left_end = x + 300
    #     dis_from_right_end = 300 - x
    #     dis_from_bottom_end = y + 300
    #     dis_from_top_end = 300 - y
    #
    #     return min(dis_from_left_end, dis_from_right_end, dis_from_bottom_end, dis_from_top_end)
