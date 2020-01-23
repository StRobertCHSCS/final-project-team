score = open('scoress.txt', 'a')
for i in range (3):
    name = input("What's ur name? ")
    high = (int(input("high score?" )))
    score.write(name + "has a high score of" + str(high) + "\n")
score.close()

score = open('scoress.txt', 'r')

for line in score:
    print (line)

