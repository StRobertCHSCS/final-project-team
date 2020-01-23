# score = open('scoress.txt', 'r+')
# score.write()
# # score.write("li7ne two")

# # score.write("line threee")

MyList = ["New York", "London", "Paris", "New Delhi"]
MyFile=open('output.txt','w')

for element in MyList:
    print >>MyFile, element
MyFile.close()