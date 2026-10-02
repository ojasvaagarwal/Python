for i in range(1,6):
    count_d = 0
    count_u = 0
    name = input(f"enter username{i} : ").strip()
    for i in name:
        if i >= chr(48) and i <= chr(57):count_d+=1
        elif i == "_":count_u+=1
        elif (i>="a" and i<="z") or (i>="A" and i<="Z"):...
        else:name+="                                                                 "

    if len(name)<=16 and name[0] in "qazxswedcvfrtgbnhyujmkiolp":
        if count_u <= 2 and count_d <= 3:print("Valid")
        else:print("Needs Improvement")
    else:print("Invalid")