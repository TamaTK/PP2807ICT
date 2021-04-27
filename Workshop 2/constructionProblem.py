# Problem: A constructor needs to estimate how much concrete is needed for a rectangular car
# park. Write a program that asks the user for the length of the park in metres, the width of
# the park in metres, and the volume of concrete required in litres per square metre. Print the
# total litres required.


length = float(input("Length of car park (m):"))
# print("Length of car park in (m) is", length)
width = float(input("Width of park (m)"))
# print("Width of car park in (m) is", width)
litreSqMtr = float(input("Litres per square metre (L):"))
print("Litres Required:", length*width*litreSqMtr)

# debugging lines
# print(type(length))
# print(type(width))
# print(type(litreSqMtr))



