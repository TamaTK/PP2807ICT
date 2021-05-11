# Problem: Write a program that prompts for the name of a file, then print the first two lines
# and the last two lines of the file.

# prompt
srcFile = input("File name: ")

# read
src = open(srcFile, 'r')
lines = src.readlines()

lastLines = lines[1], lines[2]
firstLines = lines[-2:]

print(lastLines)
print(firstLines)
