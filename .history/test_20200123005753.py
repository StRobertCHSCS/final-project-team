
from time import ctime
current_time = ctime()



# with open('scoress.txt', 'r+') as high_score_file:
#     high_scores = [0, 0, 0, 0, 0]
#     for item in high_scores:
#         high_score_file.write(str(high_scores[item]) + "\n")
#     high_score_file.close()
high_score = 0
new_score = False
with open('scoress.txt', 'r') as high_score_file:
    high_score = high_score_file.readline()

with open('scoress.txt', 'w') as high_score_file:
    current_score = (input("high score?" ))

    if current_score >= high_score:
        high_score = current_score
        high_score_file.write(str(high_score) + "\n")
        sentence = ("High score of " + str(current_score) + " at " + current_time) 
        high_score_file.write(sentence)        
    else:
        high_score = high_score



        
        



# with open('scoress.txt', 'r+') as high_score_file:
#     for i in range (7):
#         print(high_score_file.readline(i))
#         print ("--")

# for line in high_score_file:
#     print (line)

'''

import json
with open("score.json", "r+") as foo:
    for i in range (3):
        score = (input("score; "))

        json.dump(score + "\n", foo)

    #if score > int(foo.readline()):
'''
