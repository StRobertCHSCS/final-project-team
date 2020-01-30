# import json
# score = 0
# with open("high_score.json", "r") as json_file:
#     high_score = json.load(json_file)
#     scored = int(input("'./"))

# with open("high_score.json", "w") as json_file:
#     if scored > high_score:
#         json.dump(scored, json_file)
#     else:
#         json.dump(high_score, json_file)

# import time
# def time_convert(sec):
#   mins = sec // 60
#   sec = sec % 60
#   hours = mins // 60
#   mins = mins % 60
#   print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
# input("Press Enter to start")
# start_time = time.time()
# print(start_time)
# input("Press Enter to stop")
# end_time = time.time()
# time_lapsed = end_time - start_time
# time_convert(time_lapsed)

alive_button = []
start_button_text = ["Noob: 0.5 speed \n (Refresh rate 1/5 seconds)",
                    "Normal speed: 1 \n (Refresh rate 1/10 seconds)", 
                    "Hard: 1.5 speed \n (Refresh rate 1/15 seconds)", 
                    "Expert: 2.5 speed \n (Refresh rate 1/25 seconds)", 
                    "Infinite life?"]

for i in range (2, 10, 2):
        start_options = [i*100, 200, 150, 50, start_button_text[(i // 2) - 1]]  # x, y, width, height
        alive_button.append(start_options)
alive_button.append([300, 100, 150, 50, start_button_text[4]])  # x, y, width, height

print(alive_button)