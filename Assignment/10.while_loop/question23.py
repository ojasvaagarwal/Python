string = input("Enter a string : ")
length = 0
try:
    while True:
        a=string[length]
        length+=1
except IndexError:
    print(length)