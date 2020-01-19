
"""
 Simple snake example.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
 
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Snake Example')
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
 
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = segment(x, y)
 
    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
 
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
 
    allspriteslist.draw(screen)
 
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(5)
 
pygame.quit()
'''








##============================================================##
##                                                            ##
##                  Ujjwal Gupta                              ##
##                   Snake Game                               ##
##          https://github.com/ujjwalgupta07                  ##
##                                                            ##
##============================================================##


from random import randrange
import turtle

# initial heading of turtle is in east (Angle 90 in "logo" mode is east)
heading = [90]

# A list to store the postion of snake
position = []

# 0 = Food unavailable
# 1 = Fodd available
food_available = [0]

# To track the score
score = [0]

# Food co-ordinates
food_cor = [0, 0]

# Game
game_no = [0]

# Home (This function will be run first everytime a new game will start)


def home(x=0, y=0):
    turtle.clearscreen()                  # To clear the whole screen for a new game
    heading[0] = 90
    position.clear()
    food_available[0] = 0
    score[0] = 0
    food_cor[0] = 0
    food_cor[1] = 0
    turtle.mode("logo")                   # Set the turtle in mode "logo"
    turtle.setheading(heading[0])
    turtle.clear()
    turtle.up()
    turtle.hideturtle()                   # To make the turtle invisible
    turtle.title("Snake Game")            # Title of the window screen
    turtle.goto(0, 0)
    turtle.write("PLAY", align="center", font=("Arial", 15, "normal"))
    turtle.onscreenclick(start)           # Call the function start after a click on screen
    turtle.onkey(start,'space')
    turtle.done()


# To draw the outer box for the arena
def outer_box():
    turtle.clear()
    turtle.hideturtle()
    turtle.shape("square")
    turtle.speed(0)                       # Set the speed of the turtle fastest
    turtle.width(3)
    turtle.up()
    turtle.goto(332, -278)
    turtle.down()
    for i in range(2):
        turtle.left(90)
        turtle.fd(278.5*2)
        turtle.left(90)
        turtle.fd(334*2)
    turtle.up()
    turtle.goto(0, 0)
    turtle.width(1)
    turtle.speed(1)                       # Set the speed of the turtle slowest for playing the snake game


def start(x=0, y=0):
    turtle.onscreenclick(None)            # To reset the previos onscreenclick command (line 51)
    turtle.onkey(None,'space')
    x = y = 0

    outer_box()

    # Make a new turtle for food
    food_turtle = turtle.Turtle()
    food_turtle.hideturtle()
    food_turtle.up()
    food_turtle.shape("square")
    food_turtle.speed(0)
    food_turtle.color("blue")

    # Make a new turtle for score
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.up()
    score_turtle.speed(0)
    score_turtle.color("#770606")
    score_turtle.goto(291, -278)
    score_turtle.write(
        "Score: {}".format(score[0]), align="center", font=("Arial", 15, "normal"))

    # Boundary condition for snake to touch the outer box
    while x > -332 and x < 332 and y > -278 and y < 278:
        global food_available
        if food_available[0] == 0:
            food(food_turtle)
            food_available[0] = 1

        # To set the commands for arrow keys
        turtle.onkey(up, "Up")
        turtle.onkey(down, "Down")
        turtle.onkey(left, "Left")
        turtle.onkey(right, "Right")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()

        # Boundary condition for snake to eat the food
        if x - food_cor[0] < 5 and x - food_cor[0] > -5 and y - food_cor[1] < 5 and y - food_cor[1] > -5:
            food_available[0] = 0
            food_turtle.clear()
            score[0] += 1
            score_turtle.clear()
            score_turtle.write(
                "Score: {}".format(score[0]), align="center", font=("Arial", 15, "normal"))

        # Boundary condition for snake to collide with itself
        for i in range(len(position)):
            if x - position[i][0] < 5 and x - position[i][0] > -5 and y - position[i][1] < 5 and y - position[i][1] > -5:
                score_turtle.clear()
                food_turtle.clear()
                game_over()

    score_turtle.clear()
    food_turtle.clear()
    game_over()


# define the different function of arrow keys
def up(): heading[0] = 180 if heading[0] == 180 else 0


def down(): heading[0] = 0 if heading[0] == 0 else 180


def left(): heading[0] = 90 if heading[0] == 90 else 270


def right(): heading[0] = 270 if heading[0] == 270 else 90


# To create the food
def food(food_turtle):
    x = randrange(-15, 15)
    y = randrange(-12, 12)

    # The co-ordinates are multiplied with 20 so that the snake and food can be in same line
    # If co-ordinates of food will be like 211,121 then the snake and food will not be in the same line
    food_cor[0] = x*20
    food_cor[1] = y*20
    food_turtle.hideturtle()
    food_turtle.up()
    food_turtle.goto(food_cor)
    food_turtle.stamp()


# To move the snake
def move():
    turtle.setheading(heading[0])
    turtle.up()
    turtle.stamp()
    position.append(turtle.position())

    # Turtle's stamp size is 20
    # So before creating another stamp move forward 20
    turtle.fd(20)

    # Boundary conditio to check the length of snake is not more than the score + 1
    if score[0] + 1 < len(position):
        turtle.clearstamps(1)
        position.pop(0)


# Function for the game over
def game_over():
    turtle.onscreenclick(None)
    turtle.speed(0)
    game_no[0] += 1
    print("Your {} game score was : {}".format(game_no[0],score[0]))
    turtle.clear()
    turtle.hideturtle()
    turtle.up()
    turtle.color("red")
    turtle.goto(0, 175)
    turtle.write("Game Over", align="center", font=("Arial", 15, "normal"))
    turtle.goto(0, 125)
    turtle.write("Score: {}".format(score[0]),
                 align="center", font=("Arial", 15, "normal"))
    high_score()
    turtle.goto(0, -125)
    turtle.write("Click Anywhere on the screen or press \"Space\" key to go to main menu",
                 align="center", font=("Arial", 15, "normal"))
    turtle.goto(0, -175)
    turtle.write("Press 'q' to exit the game.",
                 align="center", font=("Arial", 15, "normal"))
    turtle.color("black")
    turtle.onscreenclick(home)
    turtle.onkey(home, "space")
    turtle.onkey(exit, "q")
    turtle.done()


# Function to write the high score on the screen and save it in the file high_score.txt
def high_score():
    try:
        with open(".high_score.txt", "r+") as f:
            data = int(f.read())
            if data < score[0]:
                data = score[0]
                f.seek(0)
                f.write(str(data))
                f.truncate()

            turtle.goto(0, 100)
            turtle.write("High Score: {}".format(data),
                         align="center", font=("Arial", 15, "normal"))
            turtle.goto(0, 75)
            turtle.write("To reset the high score press ' r ' key",
                         align="center", font=("Arial", 15, "normal"))
            turtle.onkey(high_reset, 'r')

    except FileNotFoundError:
    	with open(".high_score.txt",'w') as f:
    		f.write(str(score[0]))


# To reset the high score
def high_reset():
	turtle.onkey(None, 'r')
	data = 0
	with open(".high_score.txt", "r+") as f:
	    f.seek(0)
	    f.write(str(data))
	    f.truncate()
	turtle.goto(0, 0)
	turtle.write("High Score has been reset",
	             align="center", font=("Arial", 15, "normal"))


# To exit the program
def exit():
    print("Thank you for playing the game :)")
    quit()


# To start the whole game
home(0, 0)
print("Thank you for playing the game :)")
'''