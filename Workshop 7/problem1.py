# Problem: Write a program that prompts for the names of a source file to read and a target
# file to write, and copy the content of the source file to the target file, but get all empty lines
# removed, then output the number of empty lines removed.

def read_write(x, y):
    empty_count = 0
    with open(x, 'r') as source, open(y, 'w') as target:
        for line in source:
            if line.isspace():
                empty_count += 1
            else:
                target.write(line)
    print("Lines Removed: " + str(empty_count))


read_write(input("Source file name: "), input("Target file name: "))
