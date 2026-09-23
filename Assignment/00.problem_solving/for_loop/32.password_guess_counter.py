password = input("Enter password : ")
for i in range(1,6):
    mc=0
    attempt = input(f"Guess password attempt{i} : ")
    for j in range(len(password)):
        if password[j] == attempt[j]:
            mc += 1
    if mc == len(password):
        print("Correct")
        break
    else:
        print(f"Incorrect attempt, with {mc} correct characters, now {5-i} attempts left.")