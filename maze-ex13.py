from turtle import Turtle, Screen
import math

def forward():
    turtle_1.forward(10)
    boundary_check()

def right():
    turtle_1.right(90)

def left():
    turtle_1.left(90)

def backward():
    turtle_1.backward(10)
    boundary_check()

def iscollision(t1, t2):
    d = math.sqrt((t2.xcor() - t1.xcor()) ** 2 + (t2.ycor() - t1.ycor()) ** 2)
    return d < 20.0

def draw_wall(turtle, positions):
    turtle.penup()
    turtle.setposition(positions[0])
    turtle.pendown()
    for position in positions[1:]:
        turtle.setposition(position)

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('white')

screen.onkey(forward, "Up")
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(backward, "Down")
screen.listen()

# border
border = Turtle(visible=False)
border.penup()
border.pensize(3)
border.pencolor('black')
border.setposition(-450, -450)
border.pendown()
border.speed("fast")

for _ in range(4):
    border.forward(900)
    border.left(90)

# Maze
maze_1 = Turtle(visible=False)
maze_1.pensize(3)
maze_1.speed("slow")

wall_1 = [(0, -450), (300, -450), (0, -450), (0, -250), (150, -250), \
    (0, -250), (0, -50), (100, -50), (0, -50), (0, -450)]

draw_wall(maze_1, wall_1)

wall_2 = [(300, -450), (300, 100), (300, 150), (100, 150), (300, 150), \
    (300, 50), (100, 50), (300, 50), (300, -150), (100, -150), \
    (300, -150), (300, -450)]

draw_wall(maze_1, wall_2)

wall_3 = [(450, -450), (450, 450), (200, 450), (200, 400), (50, 400), \
    (50, 350), (0, 350), (0, 400), (-200, 400), (-200, 350), \
    (-275, 350), (-275, 400), (-275, 250)]

draw_wall(maze_1, wall_3)

maze_2 = Turtle(visible=False)
maze_2.pensize(3)
maze_2.speed("slow")

wall_4 = [(300, 150), (100, 150), (100, 200), (-200, 200), \
    (-200, 150), (-350, 150), (-350, 400)]

draw_wall(maze_2, wall_4)

maze_3 = Turtle(visible=False)
maze_3.pensize(3)
maze_3.speed("slow")

wall_5 = [(-275, 150), (-275, 0), (-200, 0), (-200, 50), (-150, 50), \
    (-150, 100), (-100, 100), (-100, 150), (-50, 150), (-100, 150), \
    (-100, 100), (-150, 100), (-150, 50), (-200, 50), (-200, 0), \
    (-275, 0), (-275, -150), (-350, -150), (-275, -150), (-275, -250), \
    (-350, -250), (-200, -250), (-200, -350)]

draw_wall(maze_3, wall_5)

wall_6 = [(-300, -450), (-300, -350), (-300, -450), (-100, -450), \
    (-100, -350), (-100, -450), (450, -450), (450, 250), (200, 250), \
    (450, 250), (450, 450), (300, 450), (300, 300), (300, 350), (350, 350)]

draw_wall(maze_3, wall_6)

wall_7 = [(-450, 0), (-350, 0)]

draw_wall(maze_3, wall_7)

wall_8 = [(0, -200), (-100, -200), (-100, -100), (-150, -100)]

draw_wall(maze_3, wall_8)

# end goal
goal = Turtle(shape='circle')
goal.color('gold')
goal.penup()
goal.setposition(375, -350)

turtle_1 = Turtle(shape='turtle')
turtle_1.color('black')
turtle_1.penup()
turtle_1.setposition(100, -300)

def boundary_check():
    # boundary check
    if not -450 < turtle_1.xcor() < 450 or not -450 < turtle_1.ycor() < 450:
        turtle_1.right(180)

    if iscollision(turtle_1, goal):
        goal.hideturtle()

    # if iscollision(turtle, maze_1):
    #   turtle_1.right(180)
    # if iscollision(turtle, maze_2):
    #   turtle_1.right(180)
    # if iscollision(turtle, maze_3):
    #   turtle_1.right(180)

screen.mainloop()
