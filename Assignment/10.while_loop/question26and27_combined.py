n,m = map(int,input("Enter number or rows and columns (r c) : ").split())
if m>0 and n>0:
    i = 0
    while i != n:
        j = 0
        while j != m:
            print("*",end="")
            j+=1
        print()
        i+=1