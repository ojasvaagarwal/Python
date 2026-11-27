def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)

# the code is for fibonacci number
# for mystery(4) :
#     mystery(3)+mystery(2)
#     mystery(2)+mystery(1)+mystery(1)+mystery(0)
#     mystery(1)+mystery(0)+1+1+0
#     1+0+2
#     3

# also mystery(0), mystery(1), mystery(2) = 0, 1, 1