from time import ctime
current_time = ctime()

def replace_line(file_name, line_num, text):

    lines = open(file_name, 'r').readlines()
    if len(lines) > 0:
        previous_score = file_name.readline()
        lines[line_num] = str(text + previous_score)
    else:
        lines = text

    out = open(file_name, 'w')
    out.writelines(lines + "\n")
    out.close()


with open('scoress.txt', 'a') as high_score_file:
    for i in range (1):
        high = (int(input("high score?" )))
        sentence = ("High score of " + str(high) + " at " + current_time + "\n") 
        list_score = high
        replace_line('scoress.txt', 0, list_score)
        high_score_file.write(sentence)

    high_score_file.close()


high_score_file = open('scoress.txt', 'r')
print(high_score_file.readlines())
# for line in high_score_file:
#     print (line)

