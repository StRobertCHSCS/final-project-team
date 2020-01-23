
from time import ctime
current_time = ctime()



# with open('scoress.txt', 'r+') as high_score_file:
#     high_scores = [0, 0, 0, 0, 0]
#     for item in high_scores:
#         high_score_file.write(str(high_scores[item]) + "\n")
#     high_score_file.close()
def replace_line(line_num, text):
    lines = open('scoress.txt', 'r').readlines()
    if len(lines)> 0:
        lines[0] = text
    else: 
        lines = text
    lines.close()
    
    out = open('scoress.txt', 'w')
    out.write(lines + "\n")
    out.close()

def previous_high_score():
    high_score = 0
    with open('scoress.txt', 'r') as high_score_file:
        high_score = int(high_score_file.readline())
        high_score_file.close()

def main():
    high_score = previous_high_score

    with open('scoress.txt', 'w') as high_score_file:
        current_score = int(input("high score?" ))

        if current_score > high_score:
            high_score = current_score
            high_score_file.write(str(high_score) + "\n")
            sentence = (" High score of " + str(current_score) + " at " + current_time + "\n") 
            high_score_file.write(sentence)    

main()

        
        



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
