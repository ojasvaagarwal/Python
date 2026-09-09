amt = int(input("Enter purchace amt : "))

if amt < 0:
    print("Invalid input")
elif amt<500:
    print(f"Original amount : {amt}\nDiscount percentage : {0}%\ndiscount amount : {0}\nFinal amount : {amt}")
elif amt<=999:
    print(f"Original amount : {amt}\nDiscount percentage : {5}%\ndiscount amount : {amt*0.05}\nFinal amount : {amt - (amt*0.05)}")
elif amt<=1999:
    print(f"Original amount : {amt}\nDiscount percentage : {10}%\ndiscount amount : {amt*0.1}\nFinal amount : {amt - (amt*0.1)}")
elif amt<=4999:
    print(f"Original amount : {amt}\nDiscount percentage : {15}%\ndiscount amount : {amt*0.15}\nFinal amount : {amt - (amt*0.15)}")
else:
    print(f"Original amount : {amt}\nDiscount percentage : {20}%\ndiscount amount : {amt*0.2}\nFinal amount : {amt - (amt*0.2)}")