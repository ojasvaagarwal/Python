def nmsg(msg,n):
    return "" if n==0 else msg if n==1 else msg + "\n"  + nmsg(msg,n-1)

msg = input("Enter the msg: ")
n = int(input("Repeatations: "))
print(nmsg(msg,n))