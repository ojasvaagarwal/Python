s = input("enter nums: ").split(" / ")
cc = 0
s0 = [i for i in s[0] if i.isdigit()]
for i in s[1]:
    if i in s0:
        cc+=1
        s0.remove(i)
print("Common digit count =",cc)