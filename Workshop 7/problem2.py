# Problem: Write a program that prompts for the name of a file, then print the first two lines
# and the last two lines of the file.

def line_reader(x):
    with open(x, 'r') as path:
        lines = path.read().splitlines()
        print(lines[0])
        print(lines[1])
        print(lines[-2])
        print(lines[-1])


line_reader(input("File Name: "))


""" Function uses user input as argument. Path is opened using 'with statement. We create a list by method chaining 
.read().splitlines() (reads contents of file and splits string into a list where each line is a list item.
First two lines are printed, last two lines are printed. """
