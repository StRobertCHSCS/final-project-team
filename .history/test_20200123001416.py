
# from time import ctime
# current_time = ctime()



# # with open('scoress.txt', 'r+') as high_score_file:
# #     high_scores = [0, 0, 0, 0, 0]
# #     for item in high_scores:
# #         high_score_file.write(str(high_scores[item]) + "\n")
# #     high_score_file.close()
# def replace_line(line_num, text):
#     lines = open('scoress.txt', 'r').readlines()
#     if len(lines)> 0:
#         lines[0] = text
#     else: 
#         lines = text
#     lines.close()
    
#     out = open('scoress.txt', 'w')
#     out.write(lines + "\n")
#     out.close()

# high_score = 0
# with open('scoress.txt', 'r+') as high_score_file:
#     current_score = (input("high score?" ))
#     high_score = high_score_file.readline()
#     print(high_score)

#     if current_score > high_score:

#         sentence = (" High score of " + str(current_score) + " at " + current_time + "\n") 
#         high_score_file.write(sentence)    


        
        



# # with open('scoress.txt', 'r+') as high_score_file:
# #     for i in range (7):
# #         print(high_score_file.readline(i))
# #         print ("--")

# # for line in high_score_file:
# #     print (line)

# '''

# import json
# with open("score.json", "r+") as foo:
#     for i in range (3):
#         score = (input("score; "))

#         json.dump(score + "\n", foo)

#     #if score > int(foo.readline()):
# '''
"""
Show how to use exceptions to save a high score for a game.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
 
def get_high_score():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("scoress.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
 
 
def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("scoress.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")
 
 
def main():
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()
 
    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for his/her score
        current_score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")
 
    # See if we have a new high score
    if current_score > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(current_score)
    else:
        print("Better luck next time.")
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
﻿