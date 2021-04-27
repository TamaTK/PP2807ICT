#
# Problem: The grades at a university are awarded based on the number of marks awarded for
# the course out of 100. Marks of 85 or above receive the grade of 7. Marks less than 85 but of
# 75 or above receive the grade of 6. Marks less than 75 but of 60 or above receive the grade of
# 5. Marks less than 60 but of 50 or above receive the grade of 4. Anything less than 50 gets
# the grade of F. Write a program that asks the user for the marks in number, and prints the
# grade awarded.
#


marks = float(input("How many marks?"))

if marks < 50:
    grade = "F"
elif marks < 60 >= 50:
    grade = "4"
elif marks < 75 >= 60:
    grade = "5"
elif marks < 85 >= 75:
    grade = "6"
else:
    grade = "7"

print(grade)
# print(type(grade))
