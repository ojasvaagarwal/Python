revenue = 0
for i in range(1,6):
    price = 0
    mem=input(f"is costomer{i} a member [y/n] : ").strip()
    for j in range(1,4):
        price0 = int(input(f"Enter price of item{j} : "))
        if price<0:
            print("invalid price")
            break
        price+=price0
    price0 = price
    if price >= 2000 and mem == 'y':
        price = price-price*0.2
    elif price >= 1000 and mem == 'y':
        price = price-price*0.15
    elif price >= 2000 and mem == 'n':
        price = price-price*0.15
    elif price >= 1000 and mem == 'n':
        price = price-price*0.1
    elif mem == 'y':
        price = price-price*0.05
    print(f"------------------------------------------------------------\nBill for customer{i} :-\n\tTotal bill : {price0}\n\tPay amount : {price}\n------------------------------------------------------------")
    revenue += price
print(f"------------------------------------------------------------\nRestaurant Revenue Today : {revenue}\n------------------------------------------------------------")