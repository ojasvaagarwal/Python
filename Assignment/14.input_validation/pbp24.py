bb = 10000
while True:
    wamt = int(input("Enter amount to withdraw: "))
    if 0 < wamt <= bb and wamt % 100 == 0:
        bb -= wamt
        break
    print("Amount must be positive, within balance, and a multiple of ₹100")

print(f"Withdrawn amount: ₹{wamt}")
print(f"Remaining balance: ₹{bb}")
