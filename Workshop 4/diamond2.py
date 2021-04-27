# Problem: Given an input number n, print a diamond shape with 2*n-1 rows

n = int(input("Please enter a positive integer"))

for i in range(1, n*2-1):
    i = i - (n//2-1)
    if i < 0:
        i = -i
    print(" " * i + "*" * (n - i*2) + " " * i)


