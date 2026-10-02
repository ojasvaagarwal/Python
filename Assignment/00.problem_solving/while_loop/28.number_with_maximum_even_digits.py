n=0
hn = ""
hn0 = ""
for i in range(1,11):
    even=0
    odd=0
    num = int(input(f"Enter integer{i} : "))
    num = str(num)
    for j in num:
        if j in "08642":
            even+=1
        elif j in "13579":
            odd+=1
    if even >= n:
        if even > n:
            hn=""
            n=even
            hn=hn+" "+num
        else:
            hn=hn+" "+num
print(hn)