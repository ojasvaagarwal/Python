h,m,s = map(int,input("Enter time in form of hh:mm:ss : ").split(":"))

if h>0 and h<24 and m>0 and m<60 and s>0 and s<60:
    print("Valid")
else:
    print("Invalid")