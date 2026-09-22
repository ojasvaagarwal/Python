temp = int(input("Enter temperature in celsius : "))

if temp<0:
    print("Freezing cold")
elif temp<=15:
    print("Very cold")
elif temp<=25:
    print("Cold")
elif temp<=35:
    print("Normal")
else:
    print("Hot")
