for j in range(1,6):
    email = input("Enter your email : ").strip()
    email0 = email.split("@")
    if len(email0) == 2 and "." in email0[1] and " " not in email and email0[0] != "" and email0[1][0] != "." and email0[1][-1] != ".":
        print("Valid")
    else:
        print("Invalid")