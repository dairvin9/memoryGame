# Reads information from a file and prints it out one word at a time


f = open('quoteFile.txt', 'r')

rawInput = f.read()

topics = rawInput.split('\n')

for topic in topics:
    words = topic.split(' ')
    for word in words:
        print(words)


choice = input("What would you like to study? ")
print (choice) 
