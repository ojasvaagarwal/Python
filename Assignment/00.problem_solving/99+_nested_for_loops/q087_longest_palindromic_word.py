def iz_palindrome(st):
    l = 0
    r = len(st) - 1

    while l < r:
        if st[l] != st[r]:
            return False
        l += 1
        r -= 1
    else:
        return True

s=input("enter a sentence: ").split()
r=""
for i in s:
    if iz_palindrome(i) and len(i)>len(r):
        r=i
print(r)