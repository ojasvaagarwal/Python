string = input("Enter a string : ")
count = 0
for i in string:
    if i >= chr(65) and i <= chr(90):
        count+=1
print(count)