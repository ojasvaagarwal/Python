while True:
    un = input("Enter username: ").strip()
    if len(un)>=5 and len(un.split())==1:
        break
print(f"accepted username: {un}")