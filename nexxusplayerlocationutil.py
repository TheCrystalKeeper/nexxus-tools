import turtle
import math

# List of positions and names
positions = """
763 532 VVaitFang
945 795 seenmore23
736 549 tikster
460 140 superman1987
630 678 ChrBerserk
732 514 LordCratos
504 484 super atom
510 753 7ahar
611 693 Feyre Wolfe
877 910 Woodcraft
642 803 Ariella6
761 535 JametteFighter
775 378 JB
451 695 Kathryn423
828 558 StoneDragon
293 424 whoismatt
501 226 superman-mon
682 629 ChrBerserk-mon
838 604 NexusSouth-mon
761 578 NeXXusLarge-mon


"""



# Parse the positions and names
coords = [line.split() for line in positions.strip().split('\n')]
coords = [(int(x), 1250 - int(y), name) for x, y, *name in coords]

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1500, height=1080)
screen.setworldcoordinates(0, 0, 1500, 1500)
screen.title("Turtle Graphics: Dots and Grid")

# Center the window on the screen
turtle.setup(width=1500, height=1500, startx=None, starty=None)

# Create a turtle for the grid
grid_pen = turtle.Turtle()
grid_pen.speed(0)
grid_pen.hideturtle()
grid_pen.color("lightgray")

# Draw grid
grid_size = 50
for x in range(0, 1501, grid_size):
    grid_pen.penup()
    grid_pen.goto(x, 0)
    grid_pen.pendown()
    grid_pen.goto(x, 1500)
for y in range(0, 1501, 70):
    grid_pen.penup()
    grid_pen.goto(0, y)
    grid_pen.pendown()
    grid_pen.goto(1500, y)

# Create a turtle for the dots
dot_pen = turtle.Turtle()
dot_pen.hideturtle()
dot_pen.speed(0)  # Fastest speed

# Draw the first dot (bigger and red)
red_dot = coords[0]
red_x, red_y, _ = red_dot
dot_pen.penup()
dot_pen.goto(red_x*1.25, red_y*1.25)
dot_pen.dot(15, "red")  # Larger size and red color

# Create a turtle for the names
name_pen = turtle.Turtle()
name_pen.hideturtle()
name_pen.speed(0)  # Fastest speed
name_pen.penup()
name_pen.color("black")

# Create a turtle for drawing lines
line_pen = turtle.Turtle()
line_pen.hideturtle()
line_pen.speed(0)
line_pen.color("black")

#501 226 superman-mon
#682 629 ChrBerserk-mon
#838 604 NexusSouth-mon
#761 578 NeXXusLarge-mon

# Draw the remaining dots, names, and lines
arr = [0,0,0,0]
counter = 0
for x, y, name in coords:
    counter += 1
    if (counter < 17):
        arr[0] += math.dist([x, y], [501, 226])
        arr[1] += math.dist([x, y], [682, 629])
        arr[2] += math.dist([x, y], [838, 604])
        arr[3] += math.dist([x, y], [761, 578])
arr[0] = arr[0] / 16
arr[1] = arr[1] / 16
arr[2] = arr[2] / 16
arr[3] = arr[3] / 16
counter = 0
for x, y, name in coords:
    counter += 1
    x *= 1.25
    y *= 1.25
    if (counter < 17):
        dot_pen.color("black")
    else:
        dot_pen.color("red")
    dot_pen.goto(x, y)
    dot_pen.dot()
    
    # Draw line to the red dot
    line_pen.color("lightgray")
    line_pen.penup()
    line_pen.goto(x, y)
    line_pen.pendown()
    line_pen.goto(red_x*1.25, red_y*1.25)
    line_pen.color("black")
counter = 0
for x, y, name in coords:
    counter += 1
    x *= 1.25
    y *= 1.25
    # Position for the name (slightly to the upper right of the dot)
    if (counter < 17):
        name_pen.color("black")
        name_pen.goto(x + 5, y + 5)  # Smaller offset for name
        name_pen.write(name, align="left", font=("Arial", 8, "normal"))  # Smaller font size
    else:
        name_pen.color("red")
        name_pen.goto(x + 5, y + 5)  # Smaller offset for name
        name_pen.write(" ".join(name) + " " + str(arr[counter - 17]) , align="left", font=("Arial", 8, "normal"))  # Smaller font size

# Keep the window open
turtle.done()
