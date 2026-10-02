b=int(input("Enter balance : "))
tc=0
for i in range(1,8):
    transition = (input(f"Day{i}, What to do\n\tdeposit - d\n\twithdrawal - w\n"))
    if transition == "d":
        d=int(input("Enter amt to deposit : "))
        b+=d
        print(f"amt deposited, new balance : {b}")
        tc+=1
    elif transition == "w":
        if b > 1000:
            w=int(input("Enter amt to withdraw : "))
            if b-w >= 1000:    
                b-=w
                print(f"amt withdrawed, new balance : {b}")
                tc+=1
            else:print("low balance")
        else:print("withdrawal rejected")
    else:
        print("invalid input")
print(f"final balance : {b} and transaction counts : {tc} in last 7 days.")