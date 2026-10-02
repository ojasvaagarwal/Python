for i in range(1,6):
    units = int(input(f"Enter units for consumer{i} : "))
    bill = 0
    if units<0:
        print("invalid input")
        break
    elif units<=100:
        bill = units*5
    elif units<=200:
        bill = (units-100)*7 + 500
    elif units<=400:
        bill = (units-200)*10 + 1200
    else:
        bill = (units-400)*15 + 3200
    if bill < 1000:
        print(f"Pay your low bill of : {bill}")
    elif bill <= 3000:
        print(f"Pay your medium bill of : {bill}")
    else:
        print(f"Pay your High bill of : {bill}")