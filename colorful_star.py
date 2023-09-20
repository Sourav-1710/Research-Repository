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
