high = int(input("high score?"))
score = open('scoress.txt', 'a+')

score.write(str(high))

for line in score:
    print(score, end='')