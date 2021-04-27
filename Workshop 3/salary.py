# Problem: A car dealer earns a base wage of $36.25 per hour up to their normal work week of
# 37 hours. Only whole hours are counted. If he works more hours than that (overtime) he gets
# paid at 1.5 times his normal rate for the overtime. If he sells more than 5 cars in a week, he
# gets a bonus of $200 per car from the 6th car sold. Write program to calculate the wages plus
# bonus for the car dealer in a week.

hoursWorked = int(input("How many hours were worked?"))
carsSold = int(input("How many cars were sold for the week?"))
salary = 0
bonus = 0

if hoursWorked > 37:
    salary = (hoursWorked - 37) * (36.25*1.5) + (36.25*37)

else:
    salary = hoursWorked*36.25

if carsSold > 5:
    bonus = (carsSold-5)*200

print("The salary is", salary+bonus)



