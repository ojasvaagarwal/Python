code = input("Enter product code : ").strip()
a = b = 0
if len(code) == 8:
    for i in range(3):
        if code[i] >= 'A' and code[i] <= 'Z':
            a += 1
    for j in range(3,8):
        if code[j] in '0987654321':
            b+=1
    if a+b == 8:
        print("Valid Product Code")
    else:print("Invalid Product Code")
else:print("Invalid Product Code")