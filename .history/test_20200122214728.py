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
def replace_line(line_num, text):
    lines = open(scores.txt, 'r').readlines()
    lines[line_num] = text
    out = open(scoress.txt, 'w')
    out.writelines(lines)
    out.close()

with open('scoress.txt', 'r+') as high_score_file:
    current_score = (input("high score?" ))

    for i in range(7):
        score_now = (high_score_file.readline(i))
        if current_score > (score_now):
            score_now = current_score
            sentence = ("High score of " + str(current_score) + " at " + current_time + "\n") 
            replace_line(i, str(current_score))            
            high_score_file.write(sentence)
            break
        
   

# with open('scoress.txt', 'r+') as high_score_file:
#     for i in range (7):
#         print(high_score_file.readline(i))
#         print ("--")

# for line in high_score_file:
#     print (line)

