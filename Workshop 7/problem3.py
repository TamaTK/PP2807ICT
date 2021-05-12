# Problem: Write a program that prompts for the name of a file containing numbers in each
# line, prints the average of each line. Assume each line contains numbers only and they are
# separated by spaces.

def average_of_list(lst):
    return sum(lst) / len(lst)


def numbers_from_line(str):
    return [int(digit) for digit in str.split()]


def line_average(filename):
    with open(filename, 'r') as path:
        count = 1
        for line in path:
            numbers = numbers_from_line(line)
            average = average_of_list(numbers)
            print("The average of line " + str(count) + " is " + str(average))


line_average(input("Source File: "))

""" Function average_of_list simply returns the average of the list of numbers by summing them all and dividing
by their total amount

Function numbers_from_line converts each number to an integer, splits each line of whitespace and returns this
in a list 

Function line_average iterates through each line of the file, grabs the numbers from each line using 
numbers_from line, averages them using average_of_list, and prints it out."""