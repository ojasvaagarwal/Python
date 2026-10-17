def show_square():
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

n=int(input("enter box size: "))
show_square()