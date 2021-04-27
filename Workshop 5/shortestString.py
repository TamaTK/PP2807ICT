# Problem: Write a program that prompts for and reads strings until a string starts with “A”
# is entered, then prints the shortest string that was entered. The output must match the
# punctuation in this example exactly (with quote marks).

userInput = input("Enter a String:")    # Initialising first input is important for line 6
shortest = userInput                    # The first sentence is always going to be the shortest for now.

while userInput[0] != "A":              # Sentinel value is "A". Assumption that "a" is not wanted.
    userInput = input("Enter a String:")
    if len(userInput) < len(shortest):
        shortest = userInput

print("Shortest was: " + "'" + shortest + "'")
