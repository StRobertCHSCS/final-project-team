import json
score = 0
with open("high_score.json", "r+") as json_file:
    json.dumps(score, json_file)
    high_score = json.load(json_file)
    scored = int(input("'./"))

    if scored >= high_score:
        json.dump(scored, json_file)
    else:
        json.dump(high_score, json_file)

