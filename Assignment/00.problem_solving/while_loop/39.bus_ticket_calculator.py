revenue = 0
for i in range(1,9):
    fair0 = 0
    age=int(input(f"enter passenger{i} age : "))
    dis=int(input(f"enter distance passenger{i} travels : "))
    fair0 = dis*10
    fair = fair0
    if age<0 or age>120:
        print("invalid age")
    elif age<5:
        fair=0
    elif age<=12:
        fair=fair-fair*0.5
    elif age>=60:
        fair=fair-fair*0.3
    print(f"------------------------------------------------------------\nBill for Passenger{i} :-\n\tTotal bill : {fair0}\n\tPay amount : {fair}\n------------------------------------------------------------")
    revenue += fair
print(f"------------------------------------------------------------\nBus Revenue Today : {revenue}\n------------------------------------------------------------")