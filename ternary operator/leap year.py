year = int(input("Enter a year: "))
print("It's is a Leap Year" if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else "It's not a Leap Year")

