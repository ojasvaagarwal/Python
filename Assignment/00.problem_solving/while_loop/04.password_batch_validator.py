for i in range(1,6):
    p = input(f"Enter password{i}: ")
    count = 0
    ln = 0
    u = 0
    l = 0
    d = 0
    s = 0
    if len(p) >= 8:
        ln = 1
    for j in p:
        if j >= "a" and j <= "z":
            l = 1
        elif j >= "A" and j <= "Z":
            u = 1
        elif j in "0987654321":
            d = 1
        else:
            s = 1

    count = u + l + d + s + ln

    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")
