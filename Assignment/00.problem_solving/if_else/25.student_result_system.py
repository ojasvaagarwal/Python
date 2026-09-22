marks1,marks2,marks3 = map(int,input("Enter marks of all three subjects (marks1 marks2 marks3) : ").split())
if marks1<0 and marks1>100 and marks2<0 and marks2>100 and marks3<0 and marks3>100:
    print("Invalid marks")
elif marks3<35 and marks2<35 and marks1<35:
    print("Fail")
else:
    avg = (marks2 + marks1 + marks3)/3
    if avg>=75:
        print("Distinction")
    elif avg>=60:
        print("First class")
    elif avg>=50:
        print("Second class")
    else:
        print("pass")