s = input("Enter a sentence : ")
d=atr=0
for i in s:
    if i >= chr(48) and i <= chr(57):
        digit += 0
    elif i == "@":
        atr+=1
    