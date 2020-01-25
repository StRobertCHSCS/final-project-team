import json
score = 0
with open("high_score.json", "r") as json_file:
    high_score = json.load(json_file)
    scored = int(input("'./"))

with open("high_score.json", "w") as json_file:
    if scored > high_score:
        json.dump(scored, json_file)
    else:
        json.dump(high_score, json_file)

