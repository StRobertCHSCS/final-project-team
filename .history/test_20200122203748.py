from time import ctime
current_time = ctime()

high_score_file = open('scoress.txt', 'a')
for i in range (1):
    high = (int(input("high score?" )))
    sentence = ("High score of " + str(high) + " at " + current_time + "\n") 
    # list_score = []
    # list_score.append(high)
    # high_score_file.write(sentence)
    # high_score_file.write(list_score)
high_score_file.close()


high_score_file = open('scoress.txt', 'r')
print(high_score_file.readlines())
# for line in high_score_file:
#     print (line)

