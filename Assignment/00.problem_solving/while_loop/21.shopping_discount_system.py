d20 = 0
d15 = 0
d10 = 0
d0 = 0
total = 0
total0 = 0
for i in range(1,11):
    price = int(input(f"Enter price of product{i} : "))
    total+=price
    if price<0:
        print("invalid price")
        break
    elif price >= 5000:
        price-=price*0.2
        d20+=1
    elif price >= 3000:
        price-=price*0.15
        d15+=1
    elif price >= 1000:
        price-=price*0.1
        d10+=1
    else:
        d0+=1
    total0 += price
print(f"Total pay amt = {total0:.2f}")
print(f"\n\t20 discount : {d20}\n\t15 discount : {d15}\n\t10 discount : {d10}\n\tno discount : {d0}\n")
print(f"Total discout : {total-total0:.2f}")