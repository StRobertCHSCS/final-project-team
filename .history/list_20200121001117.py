import arcade


WIDTH = 1280
HEIGHT = 730
buttons = []
show_text = False
button_text = ["Noob: 0.5 speed", "Normal speed: 1", "Hard: 1.5 speed", "Expert: 2.5 speed"]
print(buttons)

def on_update(delta_time):
    pass


def on_draw():
    global my_button
    arcade.start_render()
    # Draw in here...
    arcade.draw_text("Welcome to snake \n choose your level", 2*(WIDTH//5), 3*(HEIGHT//4), arcade.color.BLACK, 25, font_name= "comic sans")
    for i in range (2, 8, 2):
        my_button = [i*100, 200, 150, 50, button_text[i//2]]  # x, y, width, height
        buttons.append(my_button)
        arcade.draw_rectangle_filled(my_button[0],
                                        my_button[1],
                                        my_button[2],
                                        my_button[3],
                                        arcade.color.BLACK)

        arcade.draw_text(my_button[4], my_button[0], my_button[1], arcade.color.BLUE, 10, font_name= "comic sans", anchor_x="center", anchor_y="center")
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
    for i in range (len(buttons)):
        if (x > buttons[i][0] and x < buttons[i][0] + buttons[i][2] and
                y > buttons[i][1] and y < buttons[i][1] + buttons[i][3]):
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