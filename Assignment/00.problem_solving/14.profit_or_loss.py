cost_price = int(input("Cost price : "))
selling_price = int(input("Selling price : "))

if cost_price < 0 or selling_price < 0:
    print("Price can't be negetive : ")
else:
    if cost_price > selling_price:
        print("Loss")
    elif selling_price > cost_price:
        print("Profit")
    else:
        print("No loss and no profit")