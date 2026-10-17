def bill(item, quantity=1, price=100):
    return item,quantity*price
print(bill("Notebook"))
print(bill("Notebook",3))
print(bill("Notebook",3,200))
print(bill("Notebook",price=500))