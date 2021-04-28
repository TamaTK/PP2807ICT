# Problem: Roll carpet comes in rolls 3.66 meters wide. Carpet is paid for by the total number
# of whole metres that need to be cut from the roll. It may be laid in a rectangular room
# length ways or width ways. Either way there might be some wastage. The length of a room is
# always its longer dimension and its width is always its shorter dimension.
#
# Write a program that repeatedly asks the user for room dimensions until either dimension
# entered is zero or less. For each room print the length and width (to the nearest millimetre),
# and the total length of carpet required in whole metres, both length wise and width wise

import math

x = float(input("Enter Room Dimension 1 (m): "))
y = float(input("Enter Room Dimension 2 (m): "))

while x and y > 0:  # both need to be true in order to loop, therefore and statement is needed

    length = 0
    width = 0

    # Determining which way is length ways and which was is width ways

    if x > y:
        length = x
        width = y
    else:
        length = y
        width = x

    # Printing Length and Width, formatting to a millimetre point
    print("Length: " + format(length, '.3f') + "m")
    print("Width: " + format(width, '.3f') + "m")

    # If you roll the carpet length ways, this is the calculation needed.

    if width > 3.66:
        carpetsNeeded = width // 3.66
        if width % 3.66 != 0:
            carpetsNeeded += 1

    else:
        carpetsNeeded = 1

    # we need to use math.ceil to always round up the total amount of carpet needed.

    totalLength = int(math.ceil(length * carpetsNeeded))
    print("Total length required length ways = " + str(totalLength) + "m")

    carpetsNeeded = 0

    # If you roll the carpet width ways, this is the calculation needed.

    if length > 3.66:
        carpetsNeeded = length // 3.66
        if length % 3.66 != 0:
            carpetsNeeded += 1
    else:
        carpetsNeeded = 1

    carpetLength = width
    totalLength = int(carpetLength*carpetsNeeded)

    print("Total length required width ways = " + str(totalLength) + "m")

    x = float(input("Enter Room Dimension 1 (m): "))
    y = float(input("Enter Room Dimension 2 (m): "))
