fail = 0
passed = 0 
good = 0
excellent = 0
for i in range(1,11):
    num = int(input(f"Enter marks for student{i} : "))
    if num < 0 or num > 100:
        print("invalid input")
        break
    elif num < 35:
        print("Fail")
        fail+=1
    elif num < 50:
        print("Pass")
        passed+=1
    elif num < 75:
        print("Good")
        good+=1
    else:
        print("Excellent")
        excellent+=1
print(f"student who got Fail : {fail}\nstudent who got Pass : {passed}\nstudent who got Good : {good}\nstudent who got Excellent : {excellent}")