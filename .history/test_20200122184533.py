score = open("highscore.txt", "r+")

score.write("line one", "5")

score.write("line two")

score.write("line threee")

for line in score:
    print (line,)
