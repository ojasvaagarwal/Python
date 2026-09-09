cost_price = int(input("Cost price : "))
selling_price = int(input("Selling price : "))

if cost_price < 0 or selling_price < 0:
    print("Price can't be negetive : ")
else:
    if cost_price > selling_price:
        loss = cost_price - selling_price
        loss_percent = loss / cost_price * 100
        print(f"Loss\n\tloss : {loss}\n\tloss percentage : {loss_percent}")
    elif selling_price > cost_price:
        profit = cost_price - selling_price
        profit_percent = profit / cost_price * 100
        print(f"Loss\n\tprofit : {profit}\n\tprofit percentage : {profit_percent}")
    else:
        print("No loss and no profit")