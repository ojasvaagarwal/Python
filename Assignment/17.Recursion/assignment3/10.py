def palindrome(s):
    s=s.lower()
    def check(j=0,i=0):
        j=len(s)-1-i
        if i>j:return True
        if s[i]!=s[j]:return False
        return check(j,i+1)
    return check()
print(palindrome("lEvel"))
print(palindrome("naman"))
print(palindrome("naan"))
print(palindrome("car"))
print(palindrome("r"))