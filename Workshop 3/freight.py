#
# Problem: A shipping company charges its customer based on the weight of goods and the
# distance of shipping. A discount is given based on the distance of shipping as follows:
# distance < 250km, no discount
# 250 ≤ distance < 500, 10% discount
# 500 ≤ distance < 1000, 15% discount
# 1000 ≤ distance < 2000, 20% discount
# 2000 ≤ distance < 3000, 35% discount
# 3000 ≤ distance, 50% discount
# The shipping cost is calculated based on the following equation:
# cost = base price * weight * distance * (1 - discount).
# Write a program asking for input of base price, weight, and distance, and output the shipping
# cost to be charged to the customer.
#

basePrice = float(input("How much is the base price?"))
weight = float(input("What is the weight?"))
distance = float(input("What is the distance? (km)"))

if distance < 250:
    discount = 0
elif distance < 1000 >= 500:
    discount = .10
elif distance < 2000 >= 1000:
    discount = .20
elif distance < 3000 >= 2000:
    discount = .35
else:
    discount = .50

cost = basePrice * weight * distance * (1-discount)
print("The Shipping cost is", cost)
