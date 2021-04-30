# Problem: Write a program that prompts for the names of a source file to read and a target
# file to write, and copy the content of the source file to the target file, but get all empty lines
# removed, then output the number of empty lines removed.

# prompt
srcPath = input("Source file name: ")
trgPath = input("Target file name: ")

# open
try:
    src = open(srcPath, 'r')
    for line in src:
        print(line, end="")
    trg = open(trgPath, 'w')

except:
    print("Can't read/open file: ")
