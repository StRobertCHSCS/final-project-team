'''
-**make snake longer when eaten
    - fix stop watch so it restarts when you restart level
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

# Set how many rows and columns we will have
ROW_COUNT = 29
COLUMN_COUNT = 51

# WIDTH and HEIGHT of each cell, and the margin between each cell
WIDTH = 20
HEIGHT = 20
MARGIN = 5

# Determine screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

# Landing page, game, death screen, or high score
page = 0
# Intial speed refreshes once every second, changes depending on users input
SPEED = 1

# Starting screen 
# List to hold the information for the 5 buttons (x, y, length, height, buttton text)
alive_button = []
# Different text to be displayed
start_button_text = ["Noob: 0.5 speed \n (Refresh rate 1/5 seconds)",
                    "Normal speed: 1 \n (Refresh rate 1/10 seconds)", 
                    "Hard: 1.5 speed \n (Refresh rate 1/15 seconds)", 
                    "Expert: 2.5 speed \n (Refresh rate 1/25 seconds)", 
                    "Infinite life (Impossible to die)"]

# Create the buttons so they are equidistant
for i in range (2, 10, 2):
    alive_button.append([i*100, 200, 150, 50, start_button_text[(i // 2) - 1]])

# Infinite life 
alive_button.append([SCREEN_WIDTH//2 - 150, 100, 300, 50, start_button_text[4]])

# If easy mode is on, based on click from the infinite life button
easy = False


# Main game
# Direction the snake is moving in
up = False
down = False
left = False
right = False

# Snake color always changes when the game starts
snake_color = []
for i in range (3):
    snake_color.append(random.randint(0, 255))

# Use snakes position shown on grid, not the python coordinates
player_x_column = 25
player_y_row = 14 

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

# Stop watch and score, shown on the same page as the main game
time = 0
second = 0
minute = 0
score = 0


# Death screen
# Death screen buttons, same list format as the starting screen buttons
dead_button = []
death_button_text = ["Retry", "Quit"]
for x in range (2):
    dead_button.append([(2 * x + 1)*(SCREEN_WIDTH//4) - 75, (SCREEN_HEIGHT//4), 150, 150, death_button_text[(x)]])
# High score
high_score = 0

# Changing gradient colour 
red = 255
green = 255
blue = 0


def on_update(delta_time):
    snake_move()


def on_draw():
    global page 
    arcade.start_render()
    # See which functions to load depending on which page
    if page == 0:
        start_screen()
    elif page == 1:
        main_game()
    elif page == 2:
        grid_background()
        death_screen()

def start_screen():
    global alive_button, SPEED
    global easy

    arcade.draw_text("Welcome to snake \n choose your level", (SCREEN_WIDTH//2), 3*(SCREEN_HEIGHT//4), 
                    arcade.color.WHITE, 25, font_name='calibri', anchor_x="center", anchor_y="center")
    arcade.draw_text("Green = Infinite life on (Press Space to suicide) ", SCREEN_WIDTH//2, SCREEN_HEIGHT//4, 
                    arcade.color.WHITE, 25, font_name='calibri', anchor_x="center", anchor_y="center")
    arcade.draw_text("Movement keys: \n Up = W \n Down = S \n Left = A\n Right = D", 7 * (SCREEN_WIDTH//8), 3 * (SCREEN_HEIGHT//4), 
                    arcade.color.WHITE, 38, font_name='calibri', anchor_x="center", anchor_y="center")
    arcade.draw_text("If you want to suicide in game \n Press space bar", 7 * (SCREEN_WIDTH//8),  (SCREEN_HEIGHT//2), 
                    arcade.color.YELLOW, 20, font_name='calibri', anchor_x="center", anchor_y="center")
    # Draw the buttons
    for i in range (0, 4):
        arcade.draw_xywh_rectangle_filled(alive_button[i][0],
                                        alive_button[i][1],
                                        alive_button[i][2],
                                        alive_button[i][3],
                                        arcade.color.WHITE)
        arcade.draw_text(alive_button[i][4], alive_button[i][0] + (alive_button[i][2] // 2), alive_button[i][1] + (alive_button[i][3] // 2),
                            arcade.color.RICH_BLACK, 10, font_name='calibri', anchor_x="center", anchor_y="center")

    # Change colour if the infinite life button is clicked
    if easy == False:
        arcade.draw_xywh_rectangle_filled(alive_button[4][0],
                                        alive_button[4][1],
                                        alive_button[4][2],
                                        alive_button[4][3],
                                        arcade.color.RED)
    else:
        arcade.draw_xywh_rectangle_filled(alive_button[4][0],
                                            alive_button[4][1],
                                            alive_button[4][2],
                                            alive_button[4][3],
                                            arcade.color.GREEN)
    arcade.draw_text(alive_button[4][4], alive_button[4][0] + (alive_button[4][2] // 2), alive_button[4][1] + (alive_button[4][3] // 2),
                    arcade.color.BLUE, 15, font_name='calibri', anchor_x="center", anchor_y="center")
    

def snake_move():
    global player_x, player_y, player_x_column, player_y_row
    global snake_pos, easy
    global page, score

    # If infinite life on
    if easy == True:
        # Player movement
        if up:
            player_y_row += 1
        elif down:
            player_y_row -= 1
        elif right:
            player_x_column += 1
        elif left:
            player_x_column -= 1

        # Have snake reappear on other side, doesn't die when it hits wall
        if (player_x_column > COLUMN_COUNT):
            player_x_column = 0
        elif (0 > player_x_column):
            player_x_column = COLUMN_COUNT
        elif (player_y_row > ROW_COUNT):
            player_y_row = 0
        elif 0 > player_y_row:
            player_y_row = ROW_COUNT
    else:
        # Other levels, snake dies when wall is hit
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


def main_game():
    # Combine all the functions into one, easier to read
    grid_background()
    snake()
    apple()
    stop_watch()

def grid_background():
    arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, grid_texture.width, grid_texture.height, grid_texture, 0)


def snake():
    global player_x_column, player_y_row, snake_len, body
    global apple_x, apple_y
    global snake_color

    arcade.draw_rectangle_filled(player_x , player_y, WIDTH, HEIGHT, arcade.color.BLUE)
    # List of all the locations of all pieces of the snake, originally starts with the head piece
    snake_len = [[player_x_column, player_y_row]]

    # Update the location of the snakes head
    snake_pos.append([player_x_column, player_y_row])

    # Makes the snake move forward by removing the end piece
    if body < len(snake_pos):
        snake_pos.pop(0)

    # Moves all the other pieces up to the head piece 
    if (body > 1):
        for num in range (1, body):
            snake_len.append([snake_pos[num - 1][0], snake_pos[num - 1][1]])
    # Draw the snake
    for i in range (body):
        arcade.draw_rectangle_filled(
            (MARGIN + WIDTH) * snake_len[i][0] + MARGIN + WIDTH // 2, 
            (MARGIN + HEIGHT) * snake_len[i][1] + MARGIN + HEIGHT // 2 , 
            WIDTH, HEIGHT, (snake_color[0], snake_color[1], snake_color[2]))


def apple():
    global apple_x, apple_y, apple_x_coordinate, apple_y_coordinate, body, snake_len
    global score

    # Where the apple is in terms of real x, y coordinates
    apple_x_coordinate = (MARGIN + WIDTH) * apple_x + MARGIN + WIDTH // 2  
    apple_y_coordinate = (MARGIN + HEIGHT) * apple_y + MARGIN + HEIGHT // 2
    
    # See if the player has eaten the apple, if so, change locations of the apple
    if (player_x_column == apple_x) and (player_y_row == apple_y):
        apple_display = False            
        body += 1
        print ("hit")
    else:
        apple_display = True

    # Based on line 294 or 298, see what to do
    if apple_display == True:
        arcade.draw_rectangle_filled(apple_x_coordinate, apple_y_coordinate, WIDTH, HEIGHT, arcade.color.RED)
    elif apple_display == False:
        # Find a new location
        apple_x = random.randint(0, COLUMN_COUNT)
        apple_y = random.randint(0, ROW_COUNT)
        # Make sure that apple doesn't spawn where the snake is 
        for apple in range (len(snake_pos)):
                if apple_x == snake_pos[apple][0] or apple_y == snake_pos[apple][1]:
                    apple_x = random.randint(0, COLUMN_COUNT)
                    apple_y = random.randint(0, ROW_COUNT)
        # Redraw the apple in terms of real x, y coordinates
        apple_x_coordinate = (MARGIN + WIDTH) * apple_x + MARGIN + WIDTH // 2  
        apple_y_coordinate = (MARGIN + HEIGHT) * apple_y + MARGIN + HEIGHT // 2
        # Increase the score
        score += 10
        apple_display == True
        
    arcade.draw_text("Score is " + str(score), SCREEN_WIDTH - 75, SCREEN_HEIGHT - 50, arcade.color.GREEN,
                    25, font_name='calibri', bold = True, anchor_x="center", anchor_y="center")


def stop_watch():
    global time, second, minute, SPEED
    global red, green, blue

    # Time counter in minutes and seconds
    time += (60//SPEED)

    if (time % 60 == 0):
        second += 1
    elif second == 60:
        second = 0
        minute += 1

    # Flash between blue and red for stop watch text
    if second % 2 == 0:
        color = (200, 0, 0)
    else:
        color = (0, 50, 255)
    
    arcade.draw_text(f"Time played this session: {minute:02d}:{second:02d}", 25, SCREEN_HEIGHT - 50, color,
                    25, font_name='calibri', bold = True)


def death_screen():
    global dead_button, death_button_text, red, green, blue    
    global high_score, score, new_high

    # Read json file and see if our score is higher than the one stored, if so then update with our score
    with open("high_score.json", "r") as high_score_file:
        high_score = json.load(high_score_file)
    with open("high_score.json", "w") as high_score_file:
        if score > high_score:
            json.dump(score, high_score_file)
        else:
            json.dump(high_score, high_score_file)
    arcade.draw_text("The high score is " + str(high_score) + "\n  Your score is " + str(score), SCREEN_WIDTH//2, 2*(dead_button[0][1]),
                    (red, green, blue), 50, font_name='calibri', bold=True, anchor_x="center", anchor_y="center")

    # Gradient colour changing for the buttons
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
    
    # Random placing appearing text telling the user they died
    for i in range (2):
        arcade.draw_text("You died rip lol", random.randint(50, SCREEN_WIDTH), random.randint(50, SCREEN_HEIGHT), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        50, font_name='calibri', bold = True, anchor_x="center", anchor_y="center")

    # Draw the 2 option buttons
    for i in range (0, 2):
        arcade.draw_xywh_rectangle_filled(dead_button[i][0],
                                        dead_button[i][1],
                                        dead_button[i][2],
                                        dead_button[i][3],
                                        (red, blue, green))
        arcade.draw_text(dead_button[i][4], dead_button[i][0] + (dead_button[i][2] // 2), dead_button[i][1] + (dead_button[i][3] // 2),
                        arcade.color.BLACK, 15, font_name='calibri', anchor_x="center", anchor_y="center")


# If player wants to play again, reset all values
def restart():
    global player_x_column, player_y_row, snake_len, body, snake_pos
    global up, down, left, right
    global page, score
    player_x_column = 25
    player_y_row = 14
    snake_len = []
    body = 1
    snake_pos = []
    up = False
    down = False
    left = False
    right = False
    page = 1
    score = 0


def on_key_press(key, modifiers):
    global up, down, left, right
    global page

    # Movement keys and suicide key
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
        if key == arcade.key.SPACE:
            page = 2
    

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global alive_button, dead_button
    global page, restart
    global easy, SPEED

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

        elif (x > alive_button[3][0] and x < alive_button[3][0] + alive_button[3][2] and
                    y > alive_button[3][1] and y < alive_button[3][1] + alive_button[3][3]):
            page += 1
            SPEED = 25
            arcade.schedule(on_update, 1/(SPEED))
        elif (x > alive_button[4][0] and x < alive_button[4][0] + alive_button[4][2] and
                    y > alive_button[4][1] and y < alive_button[4][1] + alive_button[4][3]):
            if easy == False:
                easy = True
            else:
                easy = False


    # Options for death screen
    if page == 2:
        if (x > dead_button[0][0] and x < dead_button[0][0] + dead_button[0][2] and
                    y > dead_button[0][1] and y < dead_button[0][1] + dead_button[0][3]):
            restart()
            print("try again")

        elif (x > dead_button[1][0] and x < dead_button[1][0] + dead_button[1][2] and
                    y > dead_button[1][1] and y < dead_button[1][1] + dead_button[1][3]):
            print("exit")
            arcade.close_window()



def setup():
    global SPEED        

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "snake")
    arcade.set_background_color(arcade.color.BLACK)
    # Speed changes depending on what the player chooses
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
    