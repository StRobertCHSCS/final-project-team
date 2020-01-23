from datetime import datetime
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

score = open('scoress.txt', 'a')
for i in range (3):
    name = input("What's ur name? ")
    high = (int(input("high score?" )))
    sentence = (name + " has a high score of " + str(high) + "at" + current_time + "\n")
    score.write(sentence)
score.close()

score = open('scoress.txt', 'r')

for line in score:
    print (line)

