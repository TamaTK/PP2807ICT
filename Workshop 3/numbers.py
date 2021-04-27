# Problem: Input 3 integers, output them in descending order

a = int(input("Integer 1?"))
b = int(input("Integer 2?"))
c = int(input("Integer 3?"))

# find highest number
if a > b and a > c:
    first = a

elif b > a and b > c:
    first = b

else:
    first = c

# find lowest number
if a < b and a < c:
    third = a

elif b < a and b < c:
    third = b

else:
    third = c

# find the middle number
if a < b > c or a > b < c:
    second = a

elif b < a > c or b > a < c:
    second = b

else:
    second = c


print(first, second, third)
