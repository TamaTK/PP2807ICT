# Write a function that given a list of numbers, returns True if and only if all of the
# numbers in the list form an arithmetic progression, that is the difference between any two
# successive numbers in the list is the same. Your main program should read a file containing
# space-separated numbers as test lists, print each list and the outcome after calling the function.


def elements_to_numbers(string_list):        # function converts elements in the list to integers
    int_list = list(map(int, string_list))   # each element in given list is put into a new list as an integer element
    return int_list                          # new list returned


def arithmetic_check(lst):                   # function checks to see if integers in a list form arithmetic progression
    if lst[0] > lst[1]:                      # If first element is bigger than the next, we have a descending order.
        order = "Descending"
    elif lst[1] > lst[0]:                    # If next element is bigger than first, we have an Ascending order
        order = "Ascending"
    else:
        return False                         # Anything else returns false
    if order == "Descending":
        pattern = lst[1] - lst[0]            # When descending, the pattern becomes (2nd element - 1st element)
        for i in range(2, len(lst)):         # Check to see if the rest have the same pattern
            if lst[i] - lst[i-1] != pattern:
                return False
            else:
                pass
    else:                                    # When order is Ascending we do the same 
        pattern = lst[0] - lst[1]
        for i in range(2, len(lst)):
            if lst[i-1] - lst[i] != pattern:
                return False
            else:
                pass
    return True


def numeric_check(lst):                      # Function checks to see if each element in a list is numeric
    for element in lst:                      # returns a bool
        if element.isnumeric():
            pass
        else:
            return False
    return True


# Main Program
with open(input("File Name: "), 'r') as path:
    for line in path:
        y = line.strip()
        x = line.split()
        if numeric_check(x):
            x = elements_to_numbers(x)
            print(y, arithmetic_check(x))
        else:
            print("ERROR: Line [" + line.strip() + "] contains characters that are not space separated numbers.")
            break
        

"""The question is rather vague. '...returns true if and only if all the numbers in the list form an arithmetic 
progression.' Nowhere does it say if the numbers in the list may or may not be reordered to form an arithmetic
progression. For this problem, we assume the numbers in each list may not be reordered to form arithmetic progression.

Main program reads through each line, and uses the numeric_check, elements_to_numbers, and arithmetic_check
functions iteratively. Main program prints each line of the text file (stripped) and the arithmetic progression result
on the same line.

In the case that there are any characters in the file that are not space separated numbers, the program will end.
with an Error message."""
