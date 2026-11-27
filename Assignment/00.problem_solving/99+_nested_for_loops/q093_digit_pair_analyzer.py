def order(i,j):
    if int(i)<int(j): return "Second digit greater"
    if int(i)>int(j): return "First digit greater"
    else: return "Both are same"
a=str(int(input("enter num: ")))
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            print(f"({a[i]},{a[j]}) -",order(a[i],a[j]))

# Note: These examples assume ordered pairs of distinct digit positions, excluding pairing a digit with itself.