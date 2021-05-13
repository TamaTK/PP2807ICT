def list_compare(list1, list2):
    new_list = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                new_list.append(list1[i])

            else:
                pass
    return new_list


def unique(lst):
    list_set = set(lst)
    unique_list = (list(list_set))
    return unique_list
