def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus
print(calculate_pay(5))
print(calculate_pay(5,300))
print(calculate_pay(5,300,200))
print(calculate_pay(5,bonus=500))