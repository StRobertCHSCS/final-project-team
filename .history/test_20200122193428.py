score = open('scoress.txt', 'a')
for i in range (3):
    high = (int(input("high score?" )))
    score.write(str(high) + "\n")
score.close()

print("----")
score = open('scoress.txt', 'r+')

for line in score:
    print (line)