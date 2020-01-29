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

import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
