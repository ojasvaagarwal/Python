# 1. Division by Zero
try:
    print(10 / 0)
except ZeroDivisionError as er:
    print("ZeroDivisionError:", er)

# 2. Invalid String Operation
try:
    print("hello" - "world")
except TypeError as er:
    print("TypeError (String):", er)

# 3. Arithmetic with None
try:
    print(None + 5)
except TypeError as er:
    print("TypeError (None):", er)