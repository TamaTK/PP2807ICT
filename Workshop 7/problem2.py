# Problem: Write a program that prompts for the name of a file, then print the first two lines
# and the last two lines of the file.

# control
firstLines = 2  # Change this number, depending on how many FIRST lines you would like to print.
lastLines = 2   # Change this number, depending on how many LAST lines you would like to print.

# prompt
srcFile = input("File name: ")

# read
src = open(srcFile, 'r')


# print

for line in range(firstLines):
    print(src.readline(), end="")

for line in range(int(src) - lastLines, src):
    print

