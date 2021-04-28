# Problem: Write a function that converts all digits in a string to underline.


def converter(x):

    new_string = ""
    for i in range(len(x)):    # iterating through the length of the string
        if x[i].isnumeric():   # .isnumeric() is used to check if the "i"ish value is a number
            new_string += '_'           # since strings are immutable, use a new string instead
        else:
            new_string += x[i]

    print("Output: " + new_string)


user_input = input("Input a string?")
converter(user_input)
