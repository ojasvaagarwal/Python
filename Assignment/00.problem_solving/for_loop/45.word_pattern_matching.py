w1 = input("Enter a word1 : ").strip()
w2 = input("Enter a word2 : ").strip()
c=""
if w1 > w2:
    w = w2
else:
    w = w1
for i in range(0,len(w)):
    if w1[i] == w2[i]:
        c+="S"
    else:
        c+="D"
print(c)