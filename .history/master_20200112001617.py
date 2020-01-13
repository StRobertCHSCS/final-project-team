'''
-make snake longer when eaten
-fix player_location lists, so that the list only has the location of the current snake location, not infinite list
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


up = False
down = False
left = False
right = False

player_x_column = 5
player_y_row = 5

apple_x = random.randint(0, COLUMN_COUNT)
apple_y = random.randint(0, ROW_COUNT)

apple_display = True
player_eat = False

grid_texture = arcade.load_texture("29x51_grid.jpg")





def on_update(delta_time):
    snake_move()
    SPEED = 10

    


def on_draw():
    arcade.start_render()
    grid_background()
    snake()
    apple()

    

def grid_background():
    arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, grid_texture.width, grid_texture.height, grid_texture, 0)

    

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

        # for i in range (1):
        #     player_loaction_x = player_loaction_x(player_x_column)
        #     player_loaction_y.append(player_y_row)
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
    global player_x_column, player_y_row, player_eat, snake_len

    if player_eat:
        player_eat = False

    arcade.draw_rectangle_filled(player_x , player_y, WIDTH, HEIGHT, arcade.color.BLUE)

    snake_len = []
    snake_len.append([player_x_column, player_y_row])
    #print(snake_len)





def apple():
    global apple_x, apple_y, apple_x_coordinate, apple_y_coordinate, player_eat
    global SPEED

    apple_x_coordinate = (MARGIN + WIDTH) * apple_x + MARGIN + WIDTH // 2  
    apple_y_coordinate = (MARGIN + HEIGHT) * apple_y + MARGIN + HEIGHT // 2

    if (player_x_column == apple_x) and (player_y_row == apple_y):
        apple_display = False
        player_eat = True
    else:
        apple_display = True

    if apple_display is True:
        arcade.draw_rectangle_filled(apple_x_coordinate, apple_y_coordinate, WIDTH, HEIGHT, arcade.color.RED)
    elif apple_display is False:
        apple_x = random.randint(0, COLUMN_COUNT)
        apple_y = random.randint(0, ROW_COUNT)
        apple_x_coordinate = (MARGIN + WIDTH) * apple_x + MARGIN + WIDTH // 2  
        apple_y_coordinate = (MARGIN + HEIGHT) * apple_y + MARGIN + HEIGHT // 2
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
    global grid, SPEED


    global player_x_column, apple_x, player_y_row, apple_y, SPEED
    if (player_x_column == apple_x) and (player_y_row == apple_y):
        SPEED += 5

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "snake")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/SPEED)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press




    arcade.run()


if __name__ == '__main__':
    setup()