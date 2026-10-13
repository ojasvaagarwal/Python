while True:
    pswd = input("enter password: ")
    if len(pswd)>=8:
        break 
    print("password rejected")
print("password accepted")