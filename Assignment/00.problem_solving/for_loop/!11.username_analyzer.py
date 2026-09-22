for i in range(1,6):
    count_d = 0
    count_u = 0
    name = input(f"enter username{i} : ")
    if len(name)<=16:
        if not(name.isalnum()):
            if name[0] not in "0987654321_":
                for j in name[1:]:
                    if j in "0987654321":
                        count_d += 1
                    elif j == "_":
                        count_u += 1
                if count_d<4:
                    if count_u<3:
                        print("Valid")
                    else:print("need improvement")
                else:print("need improvement")
            else:print("Invalid")
        else:print("Invalid")
    else:print("Invalid")