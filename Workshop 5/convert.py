# Problem: Write a function that converts all digits in a string to underline.


def converter():
    user_input = input("Input a string?")
    new_string = ""
    for i in range(len(user_input)):    # iterating through the length of the string
        if user_input[i].isnumeric():   # .isnumeric() is used to check if the "i"ish value is a number
            new_string += '_'           # since strings are immutable, use a new string instead
        else:
            new_string += user_input[i]

    print("Output: " + new_string)


converter()
