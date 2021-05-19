# Write a function that given a list of numbers, rotate the numbers so the first number becomes the last, and the
# rest numbers move one position forward. Make the rotation iteratively until it returns to the initial form.

def list_rotate(lst):               # function generated new list. new lists first element will be appended to the end.
    new_list = lst                  # then, first element of new list will be removed
    new_list.append(new_list[0])
    new_list.pop(0)
    return new_list                 # new list is then returned.


def numeric_check(lst):             # function checks if each type string element in list is numeric and returns a bool
    for element in lst:
        if element.isnumeric():
            pass
        else:
            return False
    return True


numbers = input("Enter a List: ").split()

if numeric_check(numbers):
    print(numbers)
    for item in numbers:
        numbers = list_rotate(numbers)
        print(numbers)

else:
    print("Please make sure to only use digits and whitespaces. Re-run the program and try again.")
    exit()


"""Variable numbers is the user input, split into a list. Main program will check if all elements that have been
entered are numeric. Program will then print the original input without any mutations as a list, then iteratively print
  a rotated list via the list_rotate function."""