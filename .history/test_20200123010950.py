
from time import ctime
current_time = ctime()



# with open('scoress.txt', 'r+') as high_score_file:
#     high_scores = [0, 0, 0, 0, 0]
#     for item in high_scores:
#         high_score_file.write(str(high_scores[item]) + "\n")
#     high_score_file.close()
high_score = 0
new_score = False


with open('scoress.txt', 'r+') as high_score_file:
    current_score = (input("high score?" ))
    high_score = high_score_file.readline()

    if current_score > high_score:
        high_score = current_score
        new_sentence = ("High score of " + str(high_score) + " at " + current_time) 

