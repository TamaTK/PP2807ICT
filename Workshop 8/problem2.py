# Given two lists, write a function that takes these two lists as the input arguments
# and returns the list of all the elements in the first list that occur in the second list. The
# returned list shall not contain duplicate elements. Your main program will allow the user
# enter two lists of numbers and end input with a blank line for list 1.

def elements_to_numbers(collection):        # Function converts elements in given list and returns new list with
    int_list = list(map(int, collection))   # each element as an integer
    return int_list


def numeric_check(lst):                     # Checks if all string elements in a list are numeric, returns bool
    for element in lst:
        if element.isnumeric():
            pass
        else:
            return False
    return True


def unique(lst):                            # Function creates a list of unique values by converting list->set->list
    list_set = set(lst)
    unique_list = (list(list_set))
    return unique_list


def list_compare(list1, list2):             # Function iterates through two lists, if any elements are the same in
    new_list = []                           # either list, those elements will be appended to a new list.
    for i in range(len(list1)):             # Function returns new list.
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                new_list.append(list1[i])
            else:
                pass
    return new_list


sentinel = 0
while sentinel != 1:
    first = input("List 1: ").split()
    if first:

        if numeric_check(first):
            first_integers = elements_to_numbers(first)
            second = input("List 2: ").split()

            if numeric_check(second):
                second_integers = elements_to_numbers(second)
                same_nums = list_compare(first_integers, second_integers)
                output = unique(same_nums)
                print(output)

            else:
                print("Please enter a list of NUMBERS (Numbers and Whitespaces only)")

        else:
            print("Please enter a list of NUMBERS (Numbers and whitespaces only)")

    else:
        sentinel += 1

""" Main program uses a sentinel value that triggers if variable first is False (no value). 

First input is split into a list. If first input has a value AND if that value is all whitespaces and numbers, the main
program convert those elements from type string to type integer. This process is repeated with the second list.

The two list of integers are then compared using the list_compare function. A new list will be created with all
duplicate values.

Those duplicate values will be stripped using the unique function so only unique values are in the list. Unique
values are then printed. """
