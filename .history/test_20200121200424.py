dead_button = []
death_button_text = ["Retry", "Starting screen", "High scores", "Quit"]
text_num = 1
for x in range (0, 8, 4):
    for y in range (0, 6, 3):
        death_options = [x*100, y*200, 150, 150, text_num]  # x, y, width, height
        dead_button.append(death_options)
        text_num += 1
print(dead_button)