'''
-**make snake longer when eaten
    - FIGURE OUT HOW TO KNOW WHERE TO ADD THE NEXT BLOCK (MOVE LAST LOCATION TO BACK)
    DONEEE
-fix player_location lists, so that the list only has the location of the current snake location, not infinite list (done)
- fix apple so disappers when you go over it (done)
- add score (done)
-fix speed so that it resets when you go back to main page
- add high score page (txt file, saves high scores outside of program)
'''


import arcade
import random
import json




# Starting screen 
alive_button = []
start_button_text = ["Noob: 0.5 speed \n (Refresh rate 1/5 seconds)",
                    "Normal speed: 1 \n (Refresh rate 1/10 seconds)", 
                    "Hard: 1.5 speed \n (Refresh rate 1/15 seconds)", 
                    "Expert: 2.5 speed \n (Refresh rate 1/25 seconds)"]

for i in range (2, 10, 2):
        start_options = [i*100, 200, 150, 50, start_button_text[(i // 2) - 1]]  # x, y, width, height
        alive_button.append(start_options)
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

# Death screen
dead_button = []
death_button_text = ["Retry", "Starting screen", "High scores", "Quit"]
text_num = 0
for x in range (1, 5, 2):
    for y in range (1, 5, 2):
        death_options = [x*(SCREEN_WIDTH//4) - 75, y*(SCREEN_HEIGHT//4) - 75 , 150, 150, death_button_text[text_num]]  # x, y, width, height
        dead_button.append(death_options)
        text_num += 1

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
# Landing page, game, death screen, or high score
page = 0
SPEED = 1

high_score = 0
time = 0


red = 0
green = 255
blue = 0
def on_update(delta_time):


    snake_move()



def on_draw():
    global page 
    arcade.start_render()

    if page == 0:
        start_screen()
    elif page == 1:
        main_game()
    elif page == 2:
        grid_background()
        death_screen()
    elif page == 3:
        high_score_page()
    print(time)
def stop_watch():
    global time
    time += SPEED
    second = int((time //SPEED // 60))
    minute = int((time - second)//60)
    arcade.draw_text(f"Time: {minute:02d}:{second:02d}", 75, SCREEN_HEIGHT - 50, arcade.color.BLUE,
                    25, font_name='calibri', bold = True, anchor_x="center", anchor_y="center")


def high_score_check():
    global high_score, score
    
with open("high_score.json", "r") as high_score_file:
    high_score = json.load(high_score_file)

with open("high_score.json", "w") as high_score_file:
    if score > high_score:
        json.dump(score, high_score_file)
    else:
        json.dump(high_score, high_score_file)

def high_score_page():
    global high_score
    high_score_check()

    arcade.draw_text("The high score is " + str(high_score), SCREEN_WIDTH //2, SCREEN_HEIGHT // 2,
                            arcade.color.WHITE, 50, font_name='calibri', anchor_x="center", anchor_y="center")


def main_game():
    grid_background()
    snake()
    apple()
    stop_watch()



def start_screen():
    global alive_button
    arcade.draw_text("Welcome to snake \n choose your level", (SCREEN_WIDTH//2), 3*(SCREEN_HEIGHT//4), 
                    arcade.color.WHITE, 25, font_name='calibri', anchor_x="center", anchor_y="center")

    # arcade.draw_text(str(current_time), (3 * SCREEN_WIDTH // 4), (SCREEN_HEIGHT//4), 
    #         arcade.color.BLACK, 25, font_name='calibri', anchor_x="center", anchor_y="center")    


    for i in range (0, 4):
        arcade.draw_xywh_rectangle_filled(alive_button[i][0],
                                        alive_button[i][1],
                                        alive_button[i][2],
                                        alive_button[i][3],
                                        arcade.color.WHITE)

        arcade.draw_text(alive_button[i][4], alive_button[i][0] + (alive_button[i][2] // 2), alive_button[i][1] + (alive_button[i][3] // 2),
                         arcade.color.BLACK, 10, font_name='calibri', anchor_x="center", anchor_y="center")

def death_screen():
    global dead_button, death_button_text, red, green, blue

    
    if (red == 255 and 0 <= green < 255 and blue == 0):
        green += 5
    elif (0 < red <= 255 and green == 255 and blue == 0):
        red -= 5
    elif (red == 0 and green == 255 and 0 <= blue < 255):
        blue += 5
    elif (red == 0 and 0 < green <= 255 and blue == 255):
        green -= 5
    elif (0 <= red < 255 and green == 0 and blue == 255):
        red += 5
    elif (red == 255 and green == 0 and 0 < blue <= 255):
        blue -= 5
    
    for i in range (2):
        arcade.draw_text("You died rip lol", random.randint(50, SCREEN_WIDTH), random.randint(50, SCREEN_HEIGHT), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        50, font_name='calibri', bold = True, anchor_x="center", anchor_y="center")
    
    for i in range (0, 4):
        arcade.draw_xywh_rectangle_filled(dead_button[i][0],
                                        dead_button[i][1],
                                        dead_button[i][2],
                                        dead_button[i][3],
                                        (red, blue, green))
        arcade.draw_text(dead_button[i][4], dead_button[i][0] + (dead_button[i][2] // 2), dead_button[i][1] + (dead_button[i][3] // 2),
                        arcade.color.BLACK, 15, font_name='calibri', anchor_x="center", anchor_y="center")


def grid_background():
    arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, grid_texture.width, grid_texture.height, grid_texture, 0)

    
def snake_move():
    global player_x, player_y, player_x_column, player_y_row
    global snake_pos
    global page, score

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
        page = 2


    suicide_check = []
    for position in snake_pos:
        if position not in suicide_check:
            suicide_check.append(position)
        else:
            page = 2


    # Player coordinates
    player_x = (MARGIN + WIDTH) * player_x_column + MARGIN + WIDTH // 2
    player_y = (MARGIN + HEIGHT) * player_y_row + MARGIN + HEIGHT // 2


def restart():
    global player_x_column, player_y_row, snake_len, body, snake_pos
    global up, down, left, right
    global page, score, SPEED, SPEED
    player_x_column = 5
    player_y_row = 5
    snake_len = []
    body = 1
    snake_pos = []
    up = False
    down = False
    left = False
    right = False
    page = 1
    score = 0
    time = 0
    SPEED = 0
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
        score += 10
        apple_display == True
        
    arcade.draw_text("Score is " + str(score), SCREEN_WIDTH - 75, SCREEN_HEIGHT - 50, arcade.color.GREEN,
                    25, font_name='calibri', bold = True, anchor_x="center", anchor_y="center")

def on_key_press(key, modifiers):
    global up, down, left, right
    if page == 1:
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
    global alive_button, dead_button, page
    global start_screen, restart
    global high_score_page
    global SPEED

    if page == 0:
        # For starting screen, check which button has been clicked
        if (x > alive_button[0][0] and x < alive_button[0][0] + alive_button[0][2] and
                    y > alive_button[0][1] and y < alive_button[0][1] + alive_button[0][3]):
            page += 1
            SPEED = 5

            arcade.schedule(on_update, 1/(SPEED))

            print("noob")
        elif (x > alive_button[1][0] and x < alive_button[1][0] + alive_button[1][2] and
                    y > alive_button[1][1] and y < alive_button[1][1] + alive_button[1][3]):
            page += 1
            SPEED = 10
            arcade.schedule(on_update, 1/(SPEED))
            print("normal")
        elif (x > alive_button[2][0] and x < alive_button[2][0] + alive_button[2][2] and
                    y > alive_button[2][1] and y < alive_button[2][1] + alive_button[2][3]):
            page += 1
            SPEED = 15
            arcade.schedule(on_update, 1/(SPEED))

            print("hard")
        elif (x > alive_button[3][0] and x < alive_button[3][0] + alive_button[3][2] and
                    y > alive_button[3][1] and y < alive_button[3][1] + alive_button[3][3]):
            page += 1
            SPEED = 25
            arcade.schedule(on_update, 1/(SPEED))

            print("expert")
    else:
        SPEED = 1


    if page == 2:
        if (x > dead_button[0][0] and x < dead_button[0][0] + dead_button[0][2] and
                    y > dead_button[0][1] and y < dead_button[0][1] + dead_button[0][3]):
            restart()
            print("try again")

        elif (x > dead_button[1][0] and x < dead_button[1][0] + dead_button[1][2] and
                    y > dead_button[1][1] and y < dead_button[1][1] + dead_button[1][3]):
            start_screen()
            print("main")

        elif (x > dead_button[2][0] and x < dead_button[2][0] + dead_button[2][2] and
                    y > dead_button[2][1] and y < dead_button[2][1] + dead_button[2][3]):
            high_score_page()
            print("high score")
        elif (x > dead_button[3][0] and x < dead_button[3][0] + dead_button[3][2] and
                    y > dead_button[3][1] and y < dead_button[3][1] + dead_button[3][3]):
            print("exit")
            arcade.close_window()



def setup():
    global grid, SPEED

    # SPEED = float(input("What fast do you want? \n Noob: Type 0.5 \n Normal: Type 1 \n Hard: Type 1.5 - 2 \n Expert: Type 2.5 or more \n *Changes the refresh rate* \n"))
        

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
    