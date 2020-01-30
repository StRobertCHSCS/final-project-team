# # import json
# # score = 0
# # with open("high_score.json", "r") as json_file:
# #     high_score = json.load(json_file)
# #     scored = int(input("'./"))

# # with open("high_score.json", "w") as json_file:
# #     if scored > high_score:
# #         json.dump(scored, json_file)
# #     else:
# #         json.dump(high_score, json_file)

# # import time
# # def time_convert(sec):
# #   mins = sec // 60
# #   sec = sec % 60
# #   hours = mins // 60
# #   mins = mins % 60
# #   print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
# # input("Press Enter to start")
# # start_time = time.time()
# # print(start_time)
# # input("Press Enter to stop")
# # end_time = time.time()
# # time_lapsed = end_time - start_time
# # time_convert(time_lapsed)

# alive_button = []
# start_button_text = ["Noob: 0.5 speed \n (Refresh rate 1/5 seconds)",
#                     "Normal speed: 1 \n (Refresh rate 1/10 seconds)", 
#                     "Hard: 1.5 speed \n (Refresh rate 1/15 seconds)", 
#                     "Expert: 2.5 speed \n (Refresh rate 1/25 seconds)", 
#                     "Infinite life?"]

# dead_button = []
# death_button_text = ["Retry", "Quit"]
# text_num = 0
# for x in range (1, 3, 2):
#     death_options = [x*(5//4) - 75, 2*(5//4) - 75 , 150, 150, death_button_text[text_num]]  # x, y, width, height
#     dead_button.append(death_options)
#     text_num += 1
#     print (dead_button)

import os    
import time    
second = 0    
minute = 0    
hours = 0    
while(True):    
    print("Simple Stopwatch(in Python) Created By Sourabh Somani...")    
    print('\n\n\n\n\n\n\n')    
    print('\t\t\t\t-------------')    
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
    print('\t\t\t\t-------------')    
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hour+=1;    
    os.system('cls')    