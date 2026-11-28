def ct_dg(n,n0):
    if n==0:return 0
    return 1 + ct_dg(n//10,n0) if n%10==n0 else ct_dg(n//10,n0)
print(ct_dg(int(input("Enter number: ")),int(input("Enter digit to count: "))))