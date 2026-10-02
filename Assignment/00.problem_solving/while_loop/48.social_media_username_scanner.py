for j in range(1,11):
    name = input(f"Enter username{j} : ").strip()
    d=l=u=0
    for i in name:
        if i >= "0" and i <= "9":
            d+=1
        elif (i >= "A" and i <= "Z") or (i >= "a" and i <= "z"):
            l+=1
        elif i == "_":
            u+=1
        else:
            name+="                                         "
            break
    if len(name)<=16 and " " not in name:
        if u<=2 and d<=2:print("Clean")
        else:print("Acceptable")
    else:print("Invalid")