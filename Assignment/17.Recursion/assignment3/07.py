def  d_in_num(n,d):
    return True if n%10==d else False if n==0 else d_in_num(n//10)
print(d_in_num(int(input("Enter a number: "))),d_in_num(int(input("Enter digit to check: "))))