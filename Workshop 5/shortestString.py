# Problem: Write a program that prompts for and reads strings until a string starts with “A”
# is entered, then prints the shortest string that was entered. The output must match the
# punctuation in this example exactly (with quote marks).

# shortest = input("Please enter a string.")
# stopper = 0
# flag = 'A'

# while stopper == 0:

#    x = (input("Please enter another string."))

#    for i in range(x):
#        if x[i] == "A":
#           stopper = 1

x = "The Quick Brown Fox Jumped Over the Lazy Dog."

for i in range(len(x)):
    print(x[i])
