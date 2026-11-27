n=int(input("Enter size: "))
for i in range(1,n+1):
    if i%3==0 and i%5==0:print("Z",end=" ")
    elif i%3==0 :print("X",end=" ")
    elif i%5==0:print("Y",end=" ")
    else:print(i,end=" ")