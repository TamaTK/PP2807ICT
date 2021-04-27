# Problem: Write a program that reads whole numbers typed by the user until a zero is entered,
# then prints the number of positive numbers that were entered.

posCount = 0               # initialising posCount to 0 means that at this point, no positive integers have been read.
x = int(input("please enter an integer"))
while x != 0:              # 0 is sentinel value

    if x > 0:
        posCount += 1      # when the program see's the user input an integer higher than 0, posCount increments.

    x = int(input("please enter another integer"))  # input() should be at the end of the loop and nowhere else.
print(posCount, "positive numbers were entered.")
