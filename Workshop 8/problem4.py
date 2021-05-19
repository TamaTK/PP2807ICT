# Given two lists, write a function that merges these two lists in descending order.
# Your main program will allow the user enter two lists of numbers and end input with a blank
# line for list 1. You are not allowed to concatenate two lists into a new list and then call the
# built-in sort() function to sort the new list in descending order. But it is allowed to sort
# two lists in descending order before merge. Don’t worry about the complexity of the merging
# algorithm

def numeric_check(lst):                         # function checks if all elements in a list are numeric
    for element in lst:
        if element.isnumeric():
            pass
        else:
            return False
    return True


def elements_to_numbers(string_list):          # function converts all elements in a list from type str to type int
    int_list = list(map(int, string_list))
    return int_list


def manual_descend(lst):                        # function gets messy list, starts at element 0
    messy = lst
    organized = []
    while messy:                                # while we still have a messy list
        max_value = messy[0]                    # highest value is element 0
        for i in messy:                         # for each element in messy
            if i > max_value:                   # if i'sh element is bigger than the max value we have,
                max_value = i                   # max_value becomes i'ish value
        organized.append(max_value)             # we add max value to the organized list
        messy.remove(max_value)                 # remove the max value from the unorganized list
    return organized


inputOne = input("List 1: ").split()
inputTwo = input("List 2: ").split()
if numeric_check(inputOne) and numeric_check(inputTwo):
    a, b = elements_to_numbers(inputOne), elements_to_numbers(inputTwo)
    unordered = a + b
    output = manual_descend(unordered)
    print(output)

""" Program checks if list 1 and list 2 are numeric, if so, turn them into integers. We concat both unordered lists
and then begin the manual descending order process using the manual_descend function"""

