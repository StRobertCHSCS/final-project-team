score = open("highscore.txt", "r+")

score.write(linuu)

# score.write("line two")

# score.write("line threee")

for line in score:
    print (line,)
