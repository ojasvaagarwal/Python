while True:
    month = int(input("Enter month number (1-12): "))
    if 1 <= month <= 12:
        break
    print("Invalid month")
while True:
    day = int(input("Enter day number (1-31): "))
    if 1 <= day <= 31:
        break
    print("Invalid day")
print(f"Accepted month {month} and day {day}")
