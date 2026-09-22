d,m,y = map(int,input("Enter date in form of dd-mm-yyyy : ").split("-"))
if d>0 and m>0 and y>0:
    if m == 2:    
        if y%400 == 0 and d<30:
            print("Valid")
        elif y%4 == 0 and y%100 != 0 and d<30:
            print("Valid")
        elif d<29:
            print("Valid")
        else:
            print("invalid")
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if d<=31:
            print("Valid")
        else:
            print("invalid")
    elif m==4 or m==6 or m==9 or m==11 :
        if d<=30:
            print("Valid")
        else:
            print("invalid")
    else:
        print("Invalid")
else:
    print("Invalid")