import arcade
import random

# Set how many rows and columns we will have
ROW_COUNT = 25
COLUMN_COUNT = 25

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

up = False
down = False
left = False
right = False

player_x_column = 5
player_y_row = 5

texture = arcade.load_texture("white_square.jpg")

grid = []

def on_update(delta_time):
    snake_move()


def on_draw():
    arcade.start_render()
    template()
<<<<<<< HEAD

    # Draw the grid
    snake()
    apple()
=======
    #snake()
    #apple()
>>>>>>> 38a70671afe2c34a7a8ef0b7798e56a6d1a689cc
    print (player_x_column, player_y_row, SCREEN_WIDTH, SCREEN_HEIGHT)

    

def template():
    global x, y
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            # Figure out what color to draw the box
            color = arcade.color.WHITE

            # Do the math to figure out where the box is
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

            # Draw the box
<<<<<<< HEAD
            arcade.draw_texture_rectangle(x, y, texture.width, texture.height, texture)
=======
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
>>>>>>> 38a70671afe2c34a7a8ef0b7798e56a6d1a689cc

def snake_move():
    global player_x, player_y, player_x_column, player_y_row

        # Player location on grid
    #if player_x_column < ROW_COUNT:
    if up:
        player_y_row += 1
    elif down:
        player_y_row -= 1
    elif right:
        player_x_column += 1
    elif left:
        player_x_column -= 1

    # Player coordinates
    player_x = (MARGIN + WIDTH) * player_x_column + MARGIN + WIDTH // 2
    player_y = (MARGIN + HEIGHT) * player_y_row + MARGIN + HEIGHT // 2
    

def snake():
    arcade.draw_rectangle_filled(player_x, player_y, WIDTH, HEIGHT, arcade.color.BLUE)

def apple():
    apple_x = random.randint(0, COLUMN_COUNT)
    apple_y = random.randint(0, ROW_COUNT)     
    # arcade.draw_rectangle_filled(apple_x, apple_y, WIDTH, HEIGHT, arcade.color.RED)


def on_key_press(key, modifiers):
    global up, down, left, right

    if key == arcade.key.W:
        up = True
        down = False
        right = False
        left = False

    elif key == arcade.key.S:
        down = True
        up = False
        right = False
        left = False

    elif key == arcade.key.A:
        left = True 
        up = False
        down = False
        right = False

    elif key == arcade.key.D:
        right = True
        up = False
        down = False
        left = False


    
    



def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass
    

def setup():
    global grid


    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Array Backed Grids")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press



    # array is simply a list of lists.
    for row in range(ROW_COUNT):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(COLUMN_COUNT):
            grid[row].append(0)  # Append a cell

    arcade.run()


if __name__ == '__main__':
    setup()