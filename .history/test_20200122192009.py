
score = open('scoress.txt', 'a+')
for i in range (3):
    high = int(input("high score?"))
    score.write(str(high))

for line in score:
    print(score, end='')