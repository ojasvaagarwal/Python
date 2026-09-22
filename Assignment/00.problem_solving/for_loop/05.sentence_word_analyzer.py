s = input("Enter a sentence : ").split()
short = 0
medium = 0
long = 0
for i in s:
    print(i,len(i),end=" ")
    if len(i) <= 3:
        print("short")
        short+=1
    elif len(i) <= 6:
        print("medium")
        medium+=1
    else:
        print("long")
        long+=1
print(f"short : {short}\nmedium : {medium}\nlong : {long}")