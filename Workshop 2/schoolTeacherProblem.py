# Problem: A primary school needs to arrange their students to attend the National Assessment
# Program − Literacy and Numeracy test. Each school class has 25 students. A big classroom
# can accommodate 45 students, and a small classroom can accommodate 22 students. Write
# a program for the school to calculate how many full classes can be accommodated given the
# input numbers of big classrooms and small classrooms.


# sometimes it might be important to set variable, but in here it's just another line of code.
# schoolClass = 25

bigRoom = int(input("How many big classrooms?"))
smallRoom = int(input("How many small classrooms?"))
print("Number of classes =", ((bigRoom*45 + smallRoom*22) // 25))

# debugging lines
# print(type(bigRoom))
# print(type(smallRoom))
