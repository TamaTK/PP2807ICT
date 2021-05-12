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


""" With statement supports any object with __enter__() and __exit__() methods. 
When Python exists the "with" block, it will close the file after no matter how the block exits. Therefore,
there is no need to close the file with .close()

Function opens both paths and iterates through each line of the source file read. It then checks to see if
there are any lines with whitespaces only and counts them. If this is not the case, function will write the specific
line into the target file. Important to note that whatever is in the target file will be written over."""
