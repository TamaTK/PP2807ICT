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
            wordlist = line.split()
            lines += 1
            words += len(wordlist)
            chars += len(line)

    print("Characters: " + str(chars))
    print("Words: " + str(words))
    print("Lines: " + str(lines))


wc_tool(input("File Name: "))










