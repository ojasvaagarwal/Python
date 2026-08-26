text = "Python "
print(text * 3)

# String cannot be multiplied by float (raises TypeError)
try:
    print(text * 2.5)
except TypeError as er:
    print("Error:", er)