
score = open('scoress.txt', 'a+')
for i in range (3):
    high = int(input("high score?"))
    score.write(str(high), end='')

for line in score:
    print(score, )