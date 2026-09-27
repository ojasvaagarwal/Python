string = input("Enter a string : ")
length = 0
a=0
try:
    while True:
        if 'a' == string[length].lower():a+=1
        length+=1
except IndexError:
    print(a)