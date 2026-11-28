def all_ev(n):
    if n==0: return 0
    return all_ev(n-1) + n if n%2 else all_ev(n-1)

print(all_ev(int(input("Enter a number: "))))