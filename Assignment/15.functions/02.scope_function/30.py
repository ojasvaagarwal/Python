def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return item,quantity*price+delivery_fee
print(order_summary("cake",delivery_fee=50))
print(order_summary("cake"))