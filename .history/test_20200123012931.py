
# from time import ctime
# current_time = ctime()



# # with open('scoress.txt', 'r+') as high_score_file:
# #     high_scores = [0, 0, 0, 0, 0]
# #     for item in high_scores:
# #         high_score_file.write(str(high_scores[item]) + "\n")
# #     high_score_file.close()
# high_score = 0
# new_score = False


# # with open('scoress.txt', 'r+') as high_score_file:
# #     current_score = (input("high score?" ))
# #     high_score = high_score_file.read()

# #     if current_score > high_score:
# #         high_score = current_score
# #         high_score_file.write(str(current_score) + "\n")
# #         # new_sentence = ("High score of " + str(high_score) + " at " + str(current_time)) 
# #         # high_score_file.write(new_sentence)        
# #     # else:
# #         # high_score_file.write(str(high_score) + "\n")
# #         # high_score_file.write(sentence)


import json
scores = (int(input("score; ")))
high_score = 0
with open("score.json", "r") as foo:
    high_score = json.load(foo)
with open("score.json", "w") as foo:
    if scores > high_score:
        json.dump(scores, foo)
