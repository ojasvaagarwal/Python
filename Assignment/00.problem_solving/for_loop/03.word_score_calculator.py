s = input("Enter a sentence : ").split()
high_s = 0
word = ""
for i in s:
    score = 0
    for j in i:
        if j in "aeiouAEIOU":
            score+=2
        elif j in "qwrtypsdfghjklzxcvbnmQWRTYPLKJHGFDSZXCVBNM":
            score+=1
        elif j >= chr(48) and i <= chr(57):
            score+=3
        else:
            score+=4
    if score > high_s:
        high_s = score
        word = i
print(word)