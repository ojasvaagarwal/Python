n=int(input("Enter a num: "))
for i in range(n):
    i=str(i)
    l=len(i)
    s=sum(int(j)**l for j in i)
    if s==int(i):print(i,end=" ")