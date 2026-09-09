age = int(input("Enter age : "))

if age < 0:
    print("Invalid age")
elif age <18:
    print("Cannot vote")
elif age < 120:
    print("Can vote")
else:
    print("Rejected : unrealistic age")