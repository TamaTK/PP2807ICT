# Problem: Write a program that prompts for the names of a source file to read and a target
# file to write, and copy the content of the source file to the target file, but get all empty lines
# removed, then output the number of empty lines removed.

# prompt
srcPath = input("Source file name: ")
trgPath = input("Target file name: ")
emptyCounter = 0

# open and write
with open(srcPath, 'r') as src:
    with open(trgPath, 'w') as trg:
        for line in src:
            if line.isspace():
                emptyCounter += 1
            else:
                trg.write(line)
    print("Lines Removed: " + str(emptyCounter))

