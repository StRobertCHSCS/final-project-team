import arcade
import random

WIDTH = 1280
HEIGHT = 720

# Player 1
player_1_x = 10             # Player 1 paddle x location
player_1_y = HEIGHT/2       # Player 1 paddle y location
player_1_width = 10         # Player 1 paddle width
player_1_height = 144       # Player 1 paddle height
player_1_score = 0          # Player 1 score

player_1_up = False         # Player 1 up key
player_1_down = False       # Player 1 down key

# Player 2
player_2_x = 1270           # Player 2 paddle x location
player_2_y = HEIGHT/2       # Player 2 paddle y location
player_2_width = 10         # Player 2 paddle width
player_2_height = 144       # Player 2 paddle height
player_2_score = 0          # Player 2 score

player_2_up = False         # Player 2 up key
player_2_down = False       # Player 2 down key
win_text_count = 0

# Ball
ball_radius = 10            # Ball size
ball_initial_x = WIDTH/2    # Ball initial x location
ball_initial_y = HEIGHT/2   # Ball initial y location
ball_x = ball_initial_x     # Ball x location
ball_y = ball_initial_y     # Ball y position
max_speed = 10              # Maximum speed of ball
minimum_speed = 2           # Starting speed of ball
delta_x = minimum_speed     # Change in x location
delta_y = 2                 # Change in y location

# Start of round
first_to_5_wins = True      # First to score 5 times wins (Text)
ball_start = False          # Ball start movement
reset = False               # Reset positions
round_number = 1            # Number of rounds played in this game
round_number_display = True

# Flashing start text
start_text = True           # Press space to start
start_text_display = True   # Press space to start (Text)
start_text_flash = 0        # Start text flashes

# Who starts with the ball on round 1
if random.randint(0, 1) == 0:
    player_start = "Player 1"
else:
    player_start = "Player 2"

if player_start == "Player 1":
    delta_x = -minimum_speed
else:
    delta_x = minimum_speed

# End of game
# Which player has won the round
player_1_win_text = False
player_2_win_text = False

# Which player wins the game
game_over = False       # A player has won the game
player_1_win = False    # player 1 won (Text)
player_2_win = False    # player 2 won (Text)
win_text_count = 0      # Win text disappears after 10 seconds
# Restart game statistics
restart = False
restart_key = False

def on_update(delta_count):
    global player_1_up, player_1_down, player_1_y, player_1_score, player_1_win_text
    global player_2_up, player_2_down, player_2_y, player_2_score, player_2_win_text
    global ball_x, ball_y, delta_x, delta_y
    global reset, ball_start, player_start, start_text, start_text_flash, start_text_display, start_text_flash_on, start_text_flash_off, first_to_5_wins, round_number, round_number_display
    global player_1_win, player_2_win, game_over, win_text_count
    global restart_key, restart, win_text_count

# Movement within a round
    # Player 1 top border limit
    if player_1_y >= 648:
        player_1_y += 0
    elif player_1_up:
        player_1_y += 10
    # Player 1 bottom border limit
    if player_1_y <= 72:
        player_1_y -= 0
    elif player_1_down:
        player_1_y -= 10

    # Player 2 top border limit
    if player_2_y >= 648:
        player_2_y += 0
    elif player_2_up:
        player_2_y += 10
    # Player 2 bottom border limit
    if player_2_y <= 72:
        player_2_y -= 0
    elif player_2_down:
        player_2_y -= 10

    # Ball border limits
    if (ball_y == ball_radius) or (ball_y == HEIGHT - ball_radius):
        delta_y = -delta_y

    # Ball movement, game starts when space bar is pressed
    if ball_start:
        ball_x += delta_x
        ball_y += delta_y

    # Ball bounces off paddle
    # Player 1
    if (ball_x - ball_radius <= player_1_x + player_1_width) and ((player_1_y - player_1_height // 2 - ball_radius) <= ball_y <= (player_1_y + player_1_height // 2 + ball_radius)):
        delta_x = -delta_x
        if delta_x < max_speed:
            delta_x *= 1.15

    # Player 2
    elif (ball_x + ball_radius >= player_2_x - player_2_width) and (player_2_y - player_2_height // 2 - ball_radius <= ball_y <= player_2_y + player_2_height // 2 + ball_radius):
        delta_x = -delta_x
        if delta_x < max_speed:
            delta_x *= 1.15

# Round reset
    # Ball resets when past player 2 paddle (Player 1 wins)
    if ball_x - 10 >= WIDTH:
        player_1_score += 1
        player_start = "Player 2"
        reset = True
        player_1_win_text = True

    # Ball resets when past player 1 paddle (Player 2 wins)
    if ball_x + 10 <= 0:
        player_2_score += 1
        player_start = "Player 1"
        player_2_win_text = True
        reset = True

    if start_text:
        start_text_flash += 1
        if start_text_flash % 60 == 0:
            start_text_display = True
        elif (start_text_flash + 30) % 60 == 0:
            start_text_display = False
    else:
        start_text_display = False

    if reset:
        ball_x = ball_initial_x
        ball_y = ball_initial_y
        if player_start == "Player 1":
            delta_x = -minimum_speed
        else:
            delta_x = minimum_speed
        ball_start = False
        start_text = True
        player_1_y = HEIGHT / 2
        player_2_y = HEIGHT / 2
        round_number += 1
        first_to_5_wins = False
        reset = False


# Game restart
    # Which player has won the game
    if player_1_win or player_2_win:
        game_over = True

    if game_over:
        restart_key = True
        start_text = False
        reset = False
        round_number_display = False
        ball_start = False
        player_1_win_text = False
        player_2_win_text = False

    # Stop from continuously changing game over to True
    if not restart_key:
        if player_2_score < player_1_score == 5:
            player_1_win = True
        elif player_1_score < player_2_score == 5:
            player_2_win = True

    # Win text disappears
    if game_over:
        if win_text_count == 600:
            player_1_win = False
            player_2_win = False
            win_text_count = 0
        else:
            win_text_count += 1

    # Restarts game
    if restart:
        player_1_score = 0
        player_2_score = 0
        player_1_win_text = False
        player_2_win_text = False
        player_1_win = False
        player_2_win = False
        first_to_5_wins = True
        round_number = 1
        game_over = False
        start_text = True
        round_number_display = True
        restart = False


def on_draw():
    arcade.start_render()
    global first_to_5_wins, start_text_display, round_number_display
    global player_1_win_text, player_2_win_text
    global player_1_win, player_2_win, game_over

    # First to score 5 times wins
    if first_to_5_wins:
        arcade.draw_text("First to score 5 times wins", WIDTH // 2, 5 * HEIGHT // 6, arcade.color.WHITE, 45,  font_name="Comic Sans",  align="center", anchor_x="center", anchor_y="center")

    # Press start to play
    if start_text_display:
        arcade.draw_text("Press space to start", ball_initial_x, ball_initial_y, arcade.color.WHITE, 45,  font_name="Comic Sans",  align="center", anchor_x="center", anchor_y="bottom")

    # Round number
    if round_number_display:
        arcade.draw_text("Round: " + str(round_number), WIDTH // 2,  HEIGHT // 6, arcade.color.AQUA, 100, font_name="Comic Sans", align="center", anchor_x="center", anchor_y="center")

    # Player 1 or 2 has won
    if player_1_win_text:
        arcade.draw_text("Player 1 wins", 4 * WIDTH // 32, 4 * HEIGHT // 6, arcade.color.GREEN, 30, font_name="Comic Sans",  align="center", anchor_x="center", anchor_y="bottom")
    elif player_2_win_text:
        arcade.draw_text("Player 2 wins", 28 * WIDTH // 32, 4 * HEIGHT // 6, arcade.color.GREEN, 30, font_name="Comic Sans",  align="center", anchor_x="center", anchor_y="bottom")

    # Player 1 score
    arcade.draw_text(str(player_1_score), 4 * WIDTH // 32, 5 * HEIGHT // 6, arcade.color.WHITE, 75, align="center", anchor_x="center", anchor_y="center")
    # Player 2 score
    arcade.draw_text(str(player_2_score), 28 * WIDTH // 32, 5 * HEIGHT // 6, arcade.color.WHITE, 75, align="center", anchor_x="center", anchor_y="center")

    # Game won
    if player_1_win:
        arcade.draw_text("Player 1 beat player 2", WIDTH // 2,  HEIGHT // 2, arcade.color.WHITE, 85, font_name="Comic Sans", align="center", anchor_x="center", anchor_y="bottom")
    elif player_2_win:
        arcade.draw_text("Player 2 beat player 1", WIDTH // 2,  HEIGHT // 2, arcade.color.WHITE, 85, font_name="Comic Sans", align="center", anchor_x="center", anchor_y="bottom")

    # Restart game option
    if restart_key:
        arcade.draw_text("Press enter to restart", WIDTH // 2,  HEIGHT // 4, arcade.color.WHITE, 50, font_name="Comic Sans", align="center", anchor_x="center", anchor_y="bottom")

    # Ball
    arcade.draw_circle_filled(ball_x, ball_y, ball_radius, arcade.color.NEON_GREEN)

    # Player 1 paddle
    arcade.draw_rectangle_filled(player_1_x, player_1_y, player_1_width, player_1_height, arcade.color.ELECTRIC_ULTRAMARINE)

    # Player 2 paddle
    arcade.draw_rectangle_filled(player_2_x, player_2_y, player_2_width, player_2_height, arcade.color.ELECTRIC_ULTRAMARINE)


def on_key_press(key, modifiers):
    global ball_start, start_text, player_1_win_text, player_2_win_text, first_to_5_wins
    global player_1_up, player_1_down
    global player_2_up, player_2_down
    global restart_key, restart

    # Space to start, remove on screen text
    if key == arcade.key.SPACE:
        if not game_over:
            ball_start = True
            start_text = False
            player_1_win_text = False
            player_2_win_text = False
            first_to_5_wins = False
        else:
            ball_start = False

    # Player 1 movement
    if key == arcade.key.W:
        player_1_up = True
    elif key == arcade.key.S:
        player_1_down = True

    # Player 2 key press
    if key == arcade.key.UP:
        player_2_up = True
    elif key == arcade.key.DOWN:
        player_2_down = True

    # Restart game
    if restart_key:
        if key == arcade.key.ENTER:
            restart = True


def on_key_release(key, modifiers):
    global ball_start, start_text, player_1_win_text, player_2_win_text, first_to_5_wins
    global player_1_up, player_1_down
    global player_2_up, player_2_down
    global restart_key, restart

    # Space to start, remove on screen text
    if key == arcade.key.SPACE:
        if not game_over:
            ball_start = True
            start_text = False
            player_1_win_text = False
            player_2_win_text = False
            first_to_5_wins = False
        else:
            ball_start = False

    # Player 1 movement
    if key == arcade.key.W:
        player_1_up = False
    elif key == arcade.key.S:
        player_1_down = False

    # player 2 movement
    if key == arcade.key.UP:
        player_2_up = False
    elif key == arcade.key.DOWN:
        player_2_down = False

    # Restart game
    if restart_key:
        if key == arcade.key.ENTER:
            restart_key = False

def on_mouse_press(x, y, button, modifiers):
    pass

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Pong")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()

if __name__ == '__main__':
    setup()
