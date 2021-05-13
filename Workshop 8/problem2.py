def numeric_check(lst):
    for element in lst:
        if element.isnumeric():
            return True
        else:
            return False


def list_generate(string):
    lst = string.split()
    return lst


def unique(lst):
    list_set = set(lst)
    unique_list = (list(list_set))
    return unique_list


def list_compare(list1, list2):
    new_list = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                new_list.extend(list1[i])
            else:
                pass
    return new_list


sentinel = 0

while sentinel == 0:
    first = list_generate(input("List 1: "))
    if first:
        second = list_generate(input("List 2: "))
        mirrored_list = unique(
            list_compare(first, second))
        print(mirrored_list)
    else:
        sentinel = 1
