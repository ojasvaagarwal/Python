def show_pattern():
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()

n = int(input("enter size: "))
show_pattern()
show_pattern()