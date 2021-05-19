# Look for * next to name
# Add names next to name with * and name with * to a new list

def unique(lst):                            # Function creates a list of unique values by converting list->set->list
    list_set = set(lst)
    unique_list = (list(list_set))
    return unique_list


infected = []
userInput = input("File Name: ")
names = " "
with open(userInput, 'r') as path:
    for item in path:
        x = item.strip().split()
        for ele in range(len(x)):
            if x[ele].find('*') != -1:
                infected.append(x[ele])
                infected.append(x[ele-1])
                infected.append(x[ele+1])
                meeting_number = (x[0])
                print(meeting_number, names.join(infected), len(infected))

            if infected:
                for sickos in infected:
                    if sickos == x[ele]:
                        infected.append(x[ele-1])
                        infected.append(x[ele+1])
                print(unique(infected))
                print(x[0])





