# Problem: The Unix tool wc counts the numbers of characters, words and lines in a file.
# Write your own version of wc that prompts for the name of the file to read, then prints
# the counts. Assume a word may contain letters, digits, symbols and their mixture, but not
# space. Hyphenated words, e.g. large-scale, shall be considered as one word.

def wc_tool(filename):
    with open(filename, 'r') as path:
        lines = 0
        words = 0
        chars = 0

        for line in path:
            lines += 1
            wordlist = line.split()
            words += len(wordlist)
            chars += len(line)

    print("Characters: " + str(chars))
    print("Words: " + str(words))
    print("Lines: " + str(lines))


wc_tool(input("File Name: "))

""" wc_tool takes the user input as a parameter and attempts to open the file using the parameter. Firstly, we iterate
through each line in the file. Each iteration means that there must be a new line, so we just can +1 to each line. 
To get the word count, we can split each line up, and sum the length of what we've just split. Finally, the character
length is simply the sum of the length of each line. """








