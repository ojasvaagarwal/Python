marks=int(input("Enter your marks: "))

if marks>=90:
    print("Excellent")
elif 75<=marks<=89:
    print("Good")
elif 60<=marks<=74:
    print("Pass")
elif 40<=marks<=59:
    print("Average")
else:
    print("Fail")