while True:
    qty = int(input("Enter product quantity: "))
    if qty > 0:
        break
    print("Quantity must be positive")
while True:
    price = float(input("Enter unit price: "))
    if price > 0:
        break
    print("Price must be greater than zero")
print(f"Total cost: ₹{qty * price}")
