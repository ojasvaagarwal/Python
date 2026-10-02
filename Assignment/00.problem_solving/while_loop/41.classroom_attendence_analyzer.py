for i in range(1,8):
    print(f"Enter if student{i} present or absent :-")
    p=0
    a=0
    for j in range(1,6):
        at = input(f"Day{j} [P/A] : ")
        if at in "Pp":
            p+=1
        elif at in "Aa":
            a+=1
        else:
            print("Invalid input")
        total = a+p
    p = p/5*100
    if p>=90:
        print("Excelent")
    elif p>=75:
        print("Good")
    else:
        print("Warning")