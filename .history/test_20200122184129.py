score = open("highscore.txt", "r+")

score.write("line one ")

score.write("line two ")

score.write("line threee ")

print(score.readlines())
