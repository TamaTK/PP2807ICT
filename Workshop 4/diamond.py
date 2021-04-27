# Problem: Given an input number n, print a diamond shape with 2*n-1 rows

n = int(input("Please enter a Positive Integer"))

for i in range(1, n*2-1):
    if i < n:
        print(" "*(n-i), end="")    # technically printing spaces = (n - no. of rows)
        print("o"*(i*2-1))          # the amount of stars needed to print is just no. of rows*2-1


for j in range(n*2-1, n-1, -1):     # range needs to begin at -1 and end at -1 other wise middle and last row distorts
    if j >= n:                      # >= to include the final row
        print(" "*((n*2-1)-j), end="")
        print("o"*(j*2-(n*2-1)))    # I'm sure there is a better way to express this but this is working for now.
