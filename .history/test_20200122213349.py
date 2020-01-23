from time import ctime
current_time = ctime()

def replace_line(file_name, line_num, text):

    line = open(file_name, 'r')
    if len(lines) > 0:
        previous_score = line.readline()
        lines = (str(text) + previous_score)
    else:
        lines = str(text)
    print(lines)

    out = open(file_name, 'w')
    out.writelines(str(lines)+"\n")
    out.close()


# with open('scoress.txt', 'r+') as high_score_file:
#     high_scores = [0, 0, 0, 0, 0]
#     for item in high_scores:
#         high_score_file.write(str(high_scores[item]) + "\n")
#     high_score_file.close()

with open('scoress.txt', 'r+') as high_score_file:
    current_score = (int(input("high score?" )))

    for i in range(5):
        score_now = high_score_file.readline(i)
        if current_score > int(score_now):
            high_scores[i] = current_score
            sentence = ("High score of " + str(current_score) + " at " + current_time + "\n") 
            high_score_file.write(sentence)
            break
        
   




print(high_score_file.readlines())
# for line in high_score_file:
#     print (line)

