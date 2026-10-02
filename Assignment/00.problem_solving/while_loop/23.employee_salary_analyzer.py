junior = 0
mid = 0 
senior = 0
executive = 0
total = 0
for i in range(1,9):
    num = int(input(f"Enter salary for employee{i} : "))
    if num < 0:
        print("invalid input")
        break
    elif num < 25000:
        print("junior")
        junior+=1
    elif num <= 50000:
        print("Pass")
        mid+=1
    elif num <= 100000:
        print("senior")
        senior+=1
    else:
        print("executive")
        executive+=1
    total+=num
avg=total/8
print(f"employee who junior : {junior}\nemployee who mid : {mid}\nemployee who senior : {senior}\nemployee who executive : {executive}\nAvrage salary : {avg:.2f}")