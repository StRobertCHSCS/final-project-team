'''
-**make snake longer when eaten
    - FIGURE OUT HOW TO KNOW WHERE TO ADD THE NEXT BLOCK (MOVE LAST LOCATION TO BACK)
    DONEEE
-fix player_location lists, so that the list only has the location of the current snake location, not infinite list (done)
- fix apple so disappers when you go over it (done)
'''


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
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

# Direction the snake is moving in
up = False
down = False
left = False
right = False

# Use snakes position shown on grid, not the python coordinates
player_x_column = 5
player_y_row = 5

# Length of the snake body
body = 1

# Current snake location
snake_pos = []

# Determine where the starting apple will be drawn in
apple = [(random.randint(0, COLUMN_COUNT)), (random.randint(0, ROW_COUNT))]

# Boolean to see if apple needs to be moved
apple_display = True

# Background grid
grid_texture = arcade.load_texture("29x51_grid.jpg")




def on_update(delta_time):
    snake_move()


def on_draw():
    arcade.start_render()
    grid_background()
    snake()
    apple()
    

def grid_background():
    arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, grid_texture.width, grid_texture.height, grid_texture, 0)


def snake_move():
    global player_x, player_y, player_x_column, player_y_row


    if (0 <= player_x_column < COLUMN_COUNT) and (0 <= player_y_row < ROW_COUNT):
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
    snake_len = []
    body = 1
    up = False
    down = False
    left = False
    right = False
    print ("You died")


def snake():
    global player_x_column, player_y_row, apple_x, apple_y, snake_len, body


    arcade.draw_rectangle_filled(player_x , player_y, WIDTH, HEIGHT, arcade.color.BLUE)
    snake_len = [[player_x_column, player_y_row]]
    
    snake_pos.append([player_x_column, player_y_row])

    if body < len(snake_pos):
        snake_pos.pop(0)

    if (body > 1):
        for num in range (1, body):
            snake_len.append([snake_pos[num - 1][0], snake_pos[num - 1][1]])
    print(snake_len, "body", body, len(snake_pos), snake_pos)


    for i in range (body):
        arcade.draw_rectangle_filled(
            (MARGIN + WIDTH) * snake_len[i][0] + MARGIN + WIDTH // 2, 
            (MARGIN + HEIGHT) * snake_len[i][1] + MARGIN + HEIGHT // 2 , 
            WIDTH, HEIGHT, arcade.color.BLUE)


def apple():
    global apple_x, apple_y, apple_x_coordinate, apple_y_coordinate, body, snake_len
    global SPEED

    apple_x_coordinate = (MARGIN + WIDTH) * apple[0] + MARGIN + WIDTH // 2  
    apple_y_coordinate = (MARGIN + HEIGHT) * apple[1] + MARGIN + HEIGHT // 2

    if (player_x_column == apple[0]) and (player_y_row == apple[1]):
        apple_display = False            
        body += 1
        print ("hit")
    else:
        apple_display = True


    if apple_display is True:
        arcade.draw_rectangle_filled(apple_x_coordinate, apple_y_coordinate, WIDTH, HEIGHT, arcade.color.RED)
    elif apple_display is False:
        apple_x = random.randint(0, COLUMN_COUNT)
        apple_y = random.randint(0, ROW_COUNT)
        apple_x_coordinate = (MARGIN + WIDTH) * apple[0] + MARGIN + WIDTH // 2  
        apple_y_coordinate = (MARGIN + HEIGHT) * apple[1] + MARGIN + HEIGHT // 2
        apple_display == True      

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


    # global player_x_column, apple_x, player_y_row, apple_y, SPEED
    # SPEED = 10

    # if (player_x_column == apple_x) and (player_y_row == apple_y):
    #     SPEED += 5

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "snake")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/10)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press




    arcade.run()


if __name__ == '__main__':
    setup()