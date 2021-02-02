#finds where things start in strings/variables
#begins counting from 0 - infinity
#in this example, 'book' begins at index position 12
#in the real world, you could (for instance) make a spam filter with this by finding commonly used words in spam mail and sending those emails out to a spam folder

myBook = "My favorite book is 'MindF*ck'.".find('book')
print(myBook)

#if not in string, .find = -1
#if at the start of string, .find = 0
#because it returns an integer, using it for true/false is not ideal.
#however, if "book" in myBook would work for true/false
#and you can create an if statement asking if the index position = 0 

exampleUsefulness = "$$$ Get Rich Now $$$".find("$$$")

if exampleUsefulness == 0:
    print("SPAM!")
else:
    print("MAYBE NOT SPAM!")