# Problem: We’ll say that a lowercase ’g’ in a string is ”happy” if there is another ’g’ immediately
# to its left or right. Write a function to print True if all the g’s in the given string are happy,
# otherwise, print False

userString = input(str("String: "))
answer = "False"
precedence = "NULL"

if len(userString) > 1:
    for item in range(0, len(userString)-1):
        if userString[item] == 'g':
            if userString[item+1] == 'g':
                answer = "True"

            if userString[item+1] != 'g':
                precedence = "False"

if precedence == "False":
    print("Happy?: " + precedence)
else:
    print("Happy?: " + answer)

""" if precedence is false, answer will never be printed. This means that if anywhere in the string, we find
that there is a lower case g which does not have a neighbouring g, we can have the precedence variable
...take precedence over the answer we want

The program simply iterates through the string, checking to see if there are any "happy" g's. With
the two if statements on line 12, 13.

however, if the iteration finds that the g's neighbour is not a g, we will make it impossible for the the program
to print "happy?: true" with the final if/else statement

finally, its important for the iteration to end at the length of the userInput MINUS ONE. We don't need to check
the last character because technically we already check if its happy with the previously iterated character. it 
is secondly important because this way, we avoid any index error's."""
