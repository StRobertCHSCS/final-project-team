dead_button = []
death_button_text = ["Retry", "Starting screen", "High scores", "Quit"]
text_num = 1
for x in range (5, 15, 5):
    for y in range (3, 9, 3):
        death_options = [x*100, y*100, 150, 150, text_num]  # x, y, width, height
        dead_button.append(death_options)
        text_num += 1
print(dead_button)