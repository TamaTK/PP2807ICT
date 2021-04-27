# Problem: In mathematics, the Fibonacci sequence is defined such that each Fibonacci number
# is the sum of the two preceding ones, starting from 0 and 1. That is, F1 = 0, F2 = 1, F3 =
# 1, F4 = 2, ..., Fn = F(n-1) + F(n-2). Write a program that given an input n, output the first
# n Fibonacci numbers. The format of output is that at most 4 numbers can be displayed in a
# row


x = int(input("Please enter a positive integer"))

fNum1 = 0               # Fibonacci sequence ALWAYS initializes from 0 and 1.
fNum2 = 1
print(fNum1, end=' ')   # Line break is not desired, instead " ".
print(fNum2, end=' ')
count = 2               # Count set to 2 to include fNum1 and fNum2.
for i in range(x-2):
    fNext = fNum1 + fNum2   # the next Fibonacci number is always the sum of the two preceding ones.
    count += 1

    if count < 4:       # Output does not want to be fed to a new line until 4 numbers displayed on a row.
        print(fNext, end=' ')

    else:
        count = 0
        print(fNext)    # Will feed a new line by default.

    fNum1 = fNum2       # Preceding number simply changes to succeeding one.
    fNum2 = fNext

