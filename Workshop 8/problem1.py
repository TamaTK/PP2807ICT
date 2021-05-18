# Write a function that given a list of numbers, rotate the numbers so the first number becomes the last, and the
# rest numbers move one position forward. Make the rotation iteratively until it returns to the initial form.

def list_rotate(lst):
    new_list = lst
    new_list.append(new_list[0])
    new_list.pop(0)
    return new_list


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


numbers = input("Enter a List: ").split()

if numeric_check(numbers):
    print(numbers)
    for item in numbers:
        numbers = list_rotate(numbers)
        print(numbers)

else:
    print("Please make sure to only use digits and whitespaces. Re-run the program and try again.")
    exit()


""" I am toying with the concept of pure functions as I complete this workshop problem. Problem question has been
handled with list_rotate. list_rotate is iterated through for how many elements there are in the list. I have noticed
that the example for the problem begins with the user input being presented as a list initially, before being iterated
through a rotation. I have expressed this in my code by printing the list once outside of the iteration. """