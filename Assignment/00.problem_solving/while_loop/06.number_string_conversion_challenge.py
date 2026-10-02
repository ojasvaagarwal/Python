nums = ""
even = 0
odd = 0
for i in range(1,6):
    num = int(input(f"Enter number{i} : "))
    if num<0: num*-1
    num = str(num)
    for j in num:
        if j in "02468":
            even+=1
        else:
            odd+=1
if odd > even:
    print("odd digits are higher")
elif odd < even:
    print("even digits are higher")
else:
    print("equal")