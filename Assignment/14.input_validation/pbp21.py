while True:
    pswd = input("Enter password: ")
    upper = False
    lower = False
    digit = False
    space = False
    for i in pswd:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            digit = True
        if i.isspace():
            space = True
    if len(pswd) < 8:
        print("Password must have at least 8 characters")
        continue
    if upper == False:
        print("Password must have an uppercase letter")
        continue
    if lower == False:
        print("Password must have a lowercase letter")
        continue
    if digit == False:
        print("Password must have a digit")
        continue
    if space == True:
        print("Password must not contain whitespace")
        continue
    break

print("Password accepted")
