# Problem: Write a program that reads strings (without digits or symbols in the string) typed
# by the user until an empty string is entered. For each string, convert all words to lowercase,
# then sort and print the words into descending order lexicographically.

def list_converter(s):

    field = " "
    return(field.join(s))


userInput = str(input("Please enter a string (Letters Only!): "))

while userInput != "":
    w = userInput.casefold()
    x = w.replace(" ", "A")

    if x.isalpha():
        y = x.replace("A", " ")
        z = y.split()
        z.sort(reverse=True)
        print("Output: ", end="")
        print(list_converter(z))

    else:
        pass

    userInput = str(input("Please enter a string (Letters Only!): "))

""" Function list_convert will be used to convert the final list back into a string for formatting purposes."""

""" Line 15 replaces all whitespaces (which are symbols) with a capital A. Since on line 14 the program has
 already made the original contents of the string all lowercase, we can easily identify capital A's as something that
 needs to be removed later on """

""" We can now check to see if the contents of the string are only part of the alphabet on line 17, and then simply
change our capital A's back into whitespaces again"""

