def count_up(n,c=0):
    if n==c:
        return
    c+=1
    print(c)
    count_up(n,c)

count_up(3)
count_up(0)