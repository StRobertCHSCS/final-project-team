import arcade
import random

# Set how many rows and columns we will have
ROW_COUNT = 29
COLUMN_COUNT = 51

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGI

up = False
down = False
left = False
right = False

player_x_column = 5
player_y_row = 5

apple_x = (MARGIN + WIDTH) *  random.randint(0, COLUMN_COUNT) + MARGIN + WIDTH // 2
apple_y = (MARGIN + HEIGHT) * random.randint(0, ROW_COUNT) + MARGIN + HEIGHT // 2

texture = arcade.load_texture("griddd.jpg")




grid = []

def on_update(delta_time):
    snake_move()


def on_draw():
    arcade.start_render()
    grid_background()
    snake()
    apple()

    

def grid_background():
    arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, texture.width, texture.height, texture, 0)

    

def snake_move():
    global player_x, player_y, player_x_column, player_y_row


    if (0 < player_x_column < COLUMN_COUNT) and (0 < player_y_row < ROW_COUNT):
        if up:
            player_y_row += 1
        elif down:
            player_y_row -= 1
        elif right:
            player_x_column += 1
        elif left:
            player_x_column -= 1
    else:
        restart()

        

    # Player coordinates
    player_x = (MARGIN + WIDTH) * player_x_column + MARGIN + WIDTH // 2
    player_y = (MARGIN + HEIGHT) * player_y_row + MARGIN + HEIGHT // 2

def restart():
    global player_x_column, player_y_row
    global up, down, left, right
    player_x_column = 5
    player_y_row = 5
    up = False
    down = False
    left = False
    right = False
    print ("You died")

def snake():
    arcade.draw_rectangle_filled(player_x, player_y, WIDTH, HEIGHT, arcade.color.BLUE)



def apple():
    global apple_x, apple_y
    arcade.draw_rectangle_filled(apple_x, apple_y, WIDTH, HEIGHT, arcade.color.RED)


    if (player_x_column == apple_x) and (player_y_row == apple_y):
        apple_x = (MARGIN + WIDTH) *  random.randint(0, COLUMN_COUNT) + MARGIN + WIDTH // 2
        apple_y = (MARGIN + HEIGHT) * random.randint(0, ROW_COUNT) + MARGIN + HEIGHT // 2
        arcade.draw_rectangle_filled(apple_x, apple_y, WIDTH, HEIGHT, arcade.color.RED)


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


    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "snake")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/10)

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