'''
dead_button = []
death_button_text = ["Retry", "Starting screen", "High scores", "Quit"]
text_num = 0
for x in range (5, 15, 5):
    for y in range (3, 9, 3):
        death_options = [x*100, y*100, 150, 150, death_button_text[text_num]]  # x, y, width, height
        dead_button.append(death_options)
        text_num += 1

print(dead_button)
'''

'''
import pygame
import random

window_x = 300
window_y = 200

def get_rand_colour():
    colour_r = random.randint(0,255)
    colour_g = random.randint(0,255)
    colour_b = random.randint(0,255)
    return (colour_r,colour_g,colour_b)

screen = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Rainbow!")
clock = pygame.time.Clock()

done = False
counter = 0
colour = get_rand_colour()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    counter += 1
    if counter > 3:
        colour = get_rand_colour()
        counter = 0

    screen.fill(colour)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
'''

color = True
def colour():
    global red, green, blue
    red = 255
    green = 0
    blue = 0
    while (red == 255 and 0 <= green < 255 and blue == 0):
        green += 1
    # elif (0 < red <= 255 and green == 255 and blue == 0):
    #     red -= 1
    # elif (red == 0 and green == 255 and 0 <= blue < 255):
    #     blue += 1
    # elif (red == 0 and 0 < green <= 255 and blue == 255):
    #     green -= 1
    # elif (0 <= red < 255 and green == 0 and blue == 255):
    #     red += 1
    # elif (red == 255 and green == 0 and 0 < blue <= 255):
    #     blue -= 1
    #     color = False
    return  red, green, blue

while color == True:
    colour ()
    print (red, green, blue)