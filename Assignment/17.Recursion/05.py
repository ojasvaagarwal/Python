def countdown(n):
    if n==0:
        print("done")
        return
    print(n)
    countdown(n+1)

countdown(3)
countdown(0)