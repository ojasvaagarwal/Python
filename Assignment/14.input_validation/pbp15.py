while True:
    un = input("Enter username: ").strip()
    pswd = input("enter password: ")
    if len(un)>=5 and len(un.split())==1:
        break
    if len(pswd)>=8:
        break 
print(f"accepted username: {un}")
print("password accepted")