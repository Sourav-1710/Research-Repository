# Import the turtle module
import turtle

# Create a turtle screen with dimensions 500x600, starting position (0, 100)
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)

# Create a turtle object
t = turtle.Turtle()

# Create another turtle screen
s = turtle.Screen()
s.bgcolor("black")

# Set the turtle drawing speed to 5 (moderate speed)
t.speed(5)

# Define a list of colors for the star
color = ['green', 'yellow', 'blue', 'cyan']

# Initialize the color index
c = 0

# Loop to draw the star
for i in range(70):
    # Move the turtle forward based on the loop index and a multiplier
    t.forward(i * 8)

    # Turn the turtle right by 144 degrees to create a star shape
    t.right(144)

    # Set the turtle's color from the list and update the color index
    t.color(color[c])

    # Cycle through the colors in the list
    if c == 3:
        c = 0
    else:
        c += 1
        
# Keep the turtle graphics window open until closed by the user
turtle.exitonclick()
