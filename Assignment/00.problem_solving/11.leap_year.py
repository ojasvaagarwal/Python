year = int(input("Enter year to check : "))

if year%400 == 0:
    print("Leap year")
elif year%4 == 0 and year%100 != 0:
    print("Leap year")
else:
    print("Not a leap year")