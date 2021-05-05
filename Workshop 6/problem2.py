# Problem: Write a program that allows the user to enter two lists of integers, calculate the
# sum of the first and the last integers in each list, and print the larger sum. In the event of a
# tie, print Same. When there is only one integer in the list, the sum is the integer itself.

# user input
input1 = input("List One: ")
input2 = input("List Two: ")

# list conversion
list1 = input1.split()
list2 = input2.split()

# sentinel value to continue program (like example shows)
sentinel = 0
# error control
# accessing lists and summing them
while sentinel == 0:
    try:
        if len(list1) > 1:
            if len(list2) > 1:
                sum1 = int(list1[len(list1) - 1]) + int(list1[0])
                sum2 = int(list2[len(list2) - 1]) + int(list2[0])

            else:
                sum1 = int(list1[len(list1) - 1]) + int(list1[0])
                sum2 = int(list2[0])

        elif len(list2) > 1:
            sum2 = int(list2[len(list2) - 1]) + int(list2[0])
            sum1 = int(list2[0])

        else:
            sum1 = int(list1[0])
            sum2 = int(list2[0])

        if sum1 > sum2:
            print("Output: ", sum1)

        elif sum2 > sum1:
            print("Output: ", sum2)

        else:
            print("Output: Same")

    except ValueError:
        print("Please run the program again, this time only using integers & whitespaces.")
        sentinel += 1

    # repeating the process
    input1 = input("List One: ")
    input2 = input("List Two: ")
    list1 = input1.split()
    list2 = input2.split()


""" The example given in the assignment looks like it is repeated. It is a little ambiguous and I am unsure
whether to keep the program running. So, I have made anything other than whitespaces and integers unallowed and
the program will end. This is done by using a try and VALUE ERROR except error control and using a sentinel value 
to stop the program running indefinitely"""

""" Because we already know the complete length of each list and the value of each element, we can
access the last element of the list by pointing to the element that is equal to its own length-1
You can see the expressions used in 19,20,27"""

"""We use a several of if/else statements (sometimes nested) to handle all possible instances:
1: List 1 and List 2 has multiple integers (Line 19-22)
2: Only list 1 contains multiple integers (Line 24-26)
3: Only list 2 contains multiple integers (Line 28-30)
4: Neither list contains multiple integers (Line 32-34)"""

