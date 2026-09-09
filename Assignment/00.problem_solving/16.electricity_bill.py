units = int(input("Enter number of units to be paid : "))

if units < 0:
    print("invalid input")
elif units == 0:
    print("Paid")
elif units <= 100:
    print("Bill amt :",units * 5)
elif units <=200:
    units -= 100
    print("Bill amt :",(units * 7)+500)
else:
    units -= 200
    print("Bill amt :",(units * 10)+1200)