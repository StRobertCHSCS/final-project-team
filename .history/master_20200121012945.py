'''
-**make snake longer when eaten
    - FIGURE OUT HOW TO KNOW WHERE TO ADD THE NEXT BLOCK (MOVE LAST LOCATION TO BACK)
    DONEEE
-fix player_location lists, so that the list only has the location of the current snake location, not infinite list (done)
- fix apple so disappers when you go over it (done)
- add score
'''


import arcade
import random


# Starting screen 
buttons = []
button_text = ["Noob: 0.5 speed", "Normal speed: 1", "Hard: 1.5 speed", "Expert: 2.5 speed"]

for i in range (2, 10, 2):
        my_button = [i*100, 200, 150, 50, button_text[(i // 2) - 1]]  # x, y, width, height
        buttons.append(my_button)
show_text = False


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

apple_x = random.randint(0, COLUMN_COUNT)
apple_y = random.randint(0, ROW_COUNT)

# Boolean to see if apple needs to be moved
apple_display = True

# Background grid
grid_texture = arcade.load_texture("29x51_grid.jpg")

score = 0
page = 0

def on_update(delta_time):
    snake_move()


def on_draw():
    arcade.start_render()
    if page == 0:
        start_screen()
    elif page == 1:
        main_game()
    
    print(page)


def main_game():
    grid_background()
    snake()
    apple()


def start_screen():
    global buttons
    arcade.draw_text("Welcome to snake \n choose your level", 2*(SCREEN_WIDTH//5), 3*(SCREEN_HEIGHT//4), arcade.color.WHITE, 25, font_name='calibri')

    for i in range (0, 4):
        arcade.draw_xywh_rectangle_filled(buttons[i][0],
                                        buttons[i][1],
                                        buttons[i][2],
                                        buttons[i][3],
                                        arcade.color.WHITE)

        arcade.draw_text(buttons[i][4], buttons[i][0] + (buttons[i][2] // 2), buttons[i][1] + (buttons[i][3] // 2),
                         arcade.color.BLACK, 15, font_name='calibri', anchor_x="center", anchor_y="center")
    if show_text:
            print("click")
            arcade.draw_text("the button was clicked", 500, 600, arcade.color.RED, 12)
def grid_background():
    arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, grid_texture.width, grid_texture.height, grid_texture, 0)


def snake_move():
    global player_x, player_y, player_x_column, player_y_row
    global snake_pos

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

    suicide_check = []
    for position in snake_pos:
        if position not in suicide_check:
            suicide_check.append(position)
        else:
            restart()


    # Player coordinates
    player_x = (MARGIN + WIDTH) * player_x_column + MARGIN + WIDTH // 2
    player_y = (MARGIN + HEIGHT) * player_y_row + MARGIN + HEIGHT // 2


def restart():
    global player_x_column, player_y_row, snake_len, body, snake_pos
    global up, down, left, right
    player_x_column = 5
    player_y_row = 5
    snake_len = []
    body = 1
    snake_pos = []
    up = False
    down = False
    left = False
    right = False
    print ("You died")


def snake():
    global player_x_column, player_y_row, snake_len, body
    global apple_x, apple_y

    arcade.draw_rectangle_filled(player_x , player_y, WIDTH, HEIGHT, arcade.color.BLUE)
    snake_len = [[player_x_column, player_y_row]]
    
    snake_pos.append([player_x_column, player_y_row])

    if body < len(snake_pos):
        snake_pos.pop(0)

    if (body > 1):
        for num in range (1, body):
            snake_len.append([snake_pos[num - 1][0], snake_pos[num - 1][1]])

    for i in range (body):
        arcade.draw_rectangle_filled(
            (MARGIN + WIDTH) * snake_len[i][0] + MARGIN + WIDTH // 2, 
            (MARGIN + HEIGHT) * snake_len[i][1] + MARGIN + HEIGHT // 2 , 
            WIDTH, HEIGHT, arcade.color.BLUE)


def apple():
    global apple_x, apple_y, apple_x_coordinate, apple_y_coordinate, body, snake_len
    global score
    global SPEED


    apple_x_coordinate = (MARGIN + WIDTH) * apple_x + MARGIN + WIDTH // 2  
    apple_y_coordinate = (MARGIN + HEIGHT) * apple_y + MARGIN + HEIGHT // 2
    
    if (player_x_column == apple_x) and (player_y_row == apple_y):
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

        # Make sure that apple doesn't spawn where the snake is 
        for apple in range (len(snake_pos)):
                if apple_x == snake_pos[apple][0] or apple_y == snake_pos[apple][1]:
                    apple_x = random.randint(0, COLUMN_COUNT)
                    apple_y = random.randint(0, ROW_COUNT)
                    

        apple_x_coordinate = (MARGIN + WIDTH) * apple_x + MARGIN + WIDTH // 2  
        apple_y_coordinate = (MARGIN + HEIGHT) * apple_y + MARGIN + HEIGHT // 2
        apple_display == True
        score += 1      

    def high_score(score):
        arcade.draw_text("Score: " + score, 9 * (SCREEN_WIDTH//10), 3*(SCREEN_HEIGHT//4), arcade.color.WHITE, 10, font_name= "comic sans")


def on_key_press(key, modifiers):
    global up, down, left, right
    if (key == arcade.key.W) and (down == False):
        up = True
        down = False
        right = False
        left = False
    elif (key == arcade.key.S) and (up == False):
        down = True
        up = False
        right = False
        left = False
    elif (key == arcade.key.A) and (right == False):
        left = True 
        up = False
        down = False
        right = False
    elif (key == arcade.key.D) and (left == False):
        right = True
        up = False
        down = False
        left = False
    

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global show_text, my_button, page

    # For starting screen, check which button has been clicked
    if (x > buttons[0][0] and x < buttons[0][0] + buttons[0][2] and
                y > buttons[0][1] and y < buttons[0][1] + buttons[0][3]):
            show_text = True
            page += 1
            print("noob")
    elif (x > buttons[1][0] and x < buttons[1][0] + buttons[1][2] and
                y > buttons[1][1] and y < buttons[1][1] + buttons[1][3]):
            show_text = True
            page += 1
            print("normal")
    elif (x > buttons[2][0] and x < buttons[2][0] + buttons[2][2] and
                y > buttons[2][1] and y < buttons[2][1] + buttons[2][3]):
            show_text = True
            page += 1
            print("hard")
    elif (x > buttons[3][0] and x < buttons[3][0] + buttons[3][2] and
                y > buttons[3][1] and y < buttons[3][1] + buttons[3][3]):
            show_text = True
            page += 1
            print("expert")
    else:
        show_text = False


def setup():
    global grid

    SPEED = float(input("What fast do you want? \n Noob: Type 0.5 \n Normal: Type 1 \n Hard: Type 1.5 - 2 \n Expert: Type 2.5 or more \n *Changes the refresh rate* \n"))
        # global player_x_column, apple_x, player_y_row, apple_y, SPEED
        # SPEED = 10

        # if (player_x_column == apple_x) and (player_y_row == apple_y):
        #     SPEED += 5

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "snake")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/(10  * SPEED))

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press




    arcade.run()


if __name__ == '__main__':
    setup()
    