import arcade


WIDTH = 1280
HEIGHT = 730

my_button = [100, 200, 150, 50]  # x, y, width, height

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_text("Welcome to snake \n choose your level", 2*(WIDTH//5), 3*(HEIGHT//4), arcade.color.BLACK, 25, font_name= "calibiri")
    arcade.draw_text("Noob: Type 0.5 \n Normal: Type 1 \n Hard: Type 1.5 - 2 \n Expert: Type 2.5 or more \n *Changes the refresh rate* \n")

    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      arcade.color.BLACK)

    if show_text:
        arcade.draw_text("the button was clicked", 100, 300, arcade.color.RED, 12)
def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global show_text
    # unpack the button list into readable? variables.
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
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