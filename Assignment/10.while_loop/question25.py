string = input("Enter a string : ")
length = 0
a=0
try:
    while True:
        if (string[length] == string[length].upper()) and string[length].isalpha():a+=1
        length+=1
except IndexError:
    print(a)