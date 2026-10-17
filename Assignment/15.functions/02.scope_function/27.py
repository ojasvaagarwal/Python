def compare(a, b):
    if a>b:x="A is greater"
    elif a<b:x="B is greater"
    else:x="Equal"
    return x,abs(a-b)
print(compare(5,6))