import arcade


WIDTH = 1280
HEIGHT = 730
buttons = []
button_text = ["Noob: 0.5 speed", "Normal speed: 1", "Hard: 1.5 speed", "Expert: 2.5 speed"]

for i in range (2, 10, 2):
        my_button = [i*100, 200, 150, 50, button_text[(i // 2) - 1]]  # x, y, width, height
        buttons.append(my_button)
show_text = False

def on_update(delta_time):
    pass


def on_draw():
    global my_button
    arcade.start_render()
    # Draw in here...
    arcade.draw_text("Welcome to snake \n choose your level", 2*(WIDTH//5), 3*(HEIGHT//4), arcade.color.BLACK, 25, font_name= "comic sans")
    for i in range (0, 4):
        arcade.draw_rectangle_filled(buttons[i][0],
                                        buttons[i][1],
                                        buttons[i][2],
                                        buttons[i][3],
                                        arcade.color.BLACK)

        arcade.draw_text(buttons[i][4], buttons[i][0], buttons[i][1], arcade.color.BLUE, 10, font_name= "comic sans", anchor_x="center", anchor_y="center")
        if i == 8:
            break
    print(len(buttons))
    if show_text:
        arcade.draw_text("the button was clicked", 500, 600, arcade.color.RED, 12)
def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global show_text, my_button
    # unpack the button list into readable? variables.

    # Need to check all four limits of the button.
    # for i in range (len(buttons)):  
    #     if (x > buttons[i][0] and x < buttons[i][0] + buttons[i][2] and
    #             y > buttons[i][1] and y < buttons[i][1] + buttons[i][3]):
    #         show_text = True
    #     else:
    #         show_text = False

    if (x > buttons[0][0] and x < buttons[0][0] + buttons[0][2] and
                y > buttons[0][1] and y < buttons[0][1] + buttons[0][3]):
            show_text = True
    else:
        show_text = False
    elif (x > buttons[1][0] and x < buttons[1][0] + buttons[1][2] and
                y > buttons[1][1] and y < buttons[1][1] + buttons[1][3]):
            show_text = True
    else:
        show_text = False
    elif (x > buttons[2][0] and x < buttons[2][0] + buttons[2][2] and
                y > buttons[2][1] and y < buttons[2][1] + buttons[2][3]):
            show_text = True
    else:
        show_text = False
    elif (x > buttons[3][0] and x < buttons[3][0] + buttons[3][2] and
                y > buttons[3][1] and y < buttons[3][1] + buttons[3][3]):
            show_text = True
    else:
        show_text = False



def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()