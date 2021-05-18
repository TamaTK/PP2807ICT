# Given two lists, write a function that takes these two lists as the input arguments
# and returns the list of all the elements in the first list that occur in the second list. The
# returned list shall not contain duplicate elements. Your main program will allow the user
# enter two lists of numbers and end input with a blank line for list 1.

def elements_to_numbers(collection):        # function converts elements in the list to integers
    int_list = []
    for i in range(len(collection)):
        int_list.append(
            int(
                collection[i]))
    return int_list


def numeric_check(lst):
    x = 0
    for element in lst:
        if element.isnumeric():
            pass
        else:
            x += 1
    if x == 0:
        return True
    else:
        return False


def unique(lst):
    list_set = set(lst)
    unique_list = (list(list_set))
    return unique_list


def list_compare(list1, list2):
    new_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                new_list.append(list1[i])
            else:
                pass
    return new_list


sentinel = 1

while sentinel == 1:
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
                sentinel = 0

        else:
            print("Please enter a list of NUMBERS (Numbers and whitespaces only)")
            sentinel = 0

    else:
        sentinel = 0
