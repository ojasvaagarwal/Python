b=int(input("Enter balance : "))
td=tw=0
tc=int(input("Enter number of transactions : "))
for i in range(1,tc+1):
    transition = (input(f"Day{i}, What to do\n\tdeposit - d\n\twithdrawal - w\n"))
    if transition == "d":
        d=int(input("Enter amt to deposit : "))
        b+=d
        print(f"amt deposited, new balance : {b}")
        td+=1
    elif transition == "w":
        w=int(input("Enter amt to withdraw : "))
        b-=w
        print(f"amt withdrawed, new balance : {b}")
        tw+=1
print(f"total deposits : {tc}, total withdrawals : {tw} and final balance : {b}")