# Problem: Given starting and ending years, write a function to calculate the number of days
# from starting year to ending year inclusive.

def day(x, y):

    total_days = 0                 # initialising total number of days

    for i in range(x-1, y, 1):     # iterating through years, inclusive
        year = i+1                 # +1 to also check if final year is leap year.

        # A year is a leap year if it is divisible by 4, unless it is divisible by 100, unless it is
        # divisible by 400.

        if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            add = 1

        else:
            add = 0

        day_amount = 365 + add
        total_days += day_amount

        return str(total_days)


start = int(input("Year 1?"))  # First year.
end = int(input("Year 2?"))  # Second Year.
print("Days: " + day(start, end))
