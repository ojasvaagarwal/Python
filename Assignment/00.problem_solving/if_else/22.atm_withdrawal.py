act_balance = int(input("Enter account balance : "))
wd_amt = int(input("Enter withdrawal ammount : "))

if wd_amt>0 and wd_amt%100==0 and act_balance>wd_amt:
    act_balance -= wd_amt
    if act_balance < 500:
        print("insufficient balance, try increasing your balance")
    else:
        print(f"Withdrawal successful\nRemaining balance : {act_balance}")
else:
    print("Invalid input")