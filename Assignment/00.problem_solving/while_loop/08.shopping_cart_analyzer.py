budget = 0
regular = 0 
premium = 0
luxury = 0
total = 0
n=0
for i in range(1,9):
    price = float(input(f"Enter price of product{i} : "))
    if price < 0:
        print("invalid input")
        break
    elif price < 500:
        print("budget")
        budget+=1
    elif price < 2000:
        print("regular")
        regular+=1
    elif price < 5000:
        print("premium")
        premium+=1
    else:
        print("luxury")
        luxury+=1
    total+=price
    n+=1
avg = total/n
print(f"Total price : {total}\n\tbudget products : {budget}\n\tregular products : {regular}\n\tpremium products : {premium}\n\tluxury products : {luxury}\n\taverage price : {avg}")