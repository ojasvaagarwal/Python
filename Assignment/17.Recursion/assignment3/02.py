def all_ev(n):
    if n==0: return
    all_ev(n-1)
    if not n%2:print(n,end=" ")

all_ev(int(input("Enter a number: ")))