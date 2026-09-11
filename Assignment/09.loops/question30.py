for i in range(1,6):
    for j in range(1,6):
        if i*j<10:
            print("0",i*j,sep="",end=" | ")
        else:
            print(i*j,end=" | ")
    print()