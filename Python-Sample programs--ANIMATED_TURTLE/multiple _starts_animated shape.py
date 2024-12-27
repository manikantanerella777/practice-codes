#multiple starts 

from turtle import Turtle, Screen

def rStars(turtle, size):
    if size < 11:  # Stop drawing smaller stars when size is below threshold
        return

    turtle.begin_fill()
    turtle.fillcolor("red")
    for i in range(5):  # Draw a star with recursive smaller stars
        turtle.forward(size)
        rStars(turtle, size / 3)  # Recursive call for smaller stars
        turtle.right(144)
    turtle.end_fill()

def pressCancel():
    p = Screen().textinput("Next Shape", "Press cancel to exit")  # Prompt input
    if p is None:  # Exit if cancel is pressed
        Screen().bye()
        return True
    return False

if __name__ == "__main__":  # Correct main function check
    screen = Screen()
    screen.setup(640, 550, 0, 0)

    t = Turtle()
    t.penup()
    t.goto(-100, 100)
    t.pendown()

    rStars(t, 45)  # Draw recursive stars
    t.hideturtle()

    pressCancel()
