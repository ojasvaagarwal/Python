# None represents absence of value, so arithmetic operations give TypeError
value = None
a = 10

try:
    print(value + a)
except TypeError as er:
    print("Error with None:", er)