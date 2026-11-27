def palindrome(s):
    s=s.lower()
    j=len(s)-1
    def check(j,i=0):
        if i>j:return True
        if s[i]!=s[j]:return False
        i+=1
        j-=1
        return check(j,i)
    return check(j)
print(palindrome("lEvel"))
print(palindrome("naman"))
print(palindrome("naan"))
print(palindrome("car"))
print(palindrome("r"))