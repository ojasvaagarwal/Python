s = input("Enter a sentence : ")
for i in s:
    for j in i:
        if j >= chr(48) and j <= chr(57):
            digit = True
        elif j == "@":
            digit = True
        