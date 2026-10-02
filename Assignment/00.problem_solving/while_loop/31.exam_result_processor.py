fail=0
failed = 0
pas=0
hp=0
tp=""
lp=100
ls=""
for i in range(1,6):
    name = input(f"Enter student{i} name : ")
    total = 0
    for j in range(1,6):
        num = int(input(f"Enter marks{j} for student{i} : "))
        if num < 0 or num > 100:
            print("invalid input")
            break
        elif num < 35:
            print("Fail")
            fail+=1
        else:
            print("Pass")
        if num < 35:
            print("F")
        elif num < 50:
            print("E")
        elif num < 60:
            print("D")
        elif num < 80:
            print("C")
        elif num < 90:
            print("B")
        else:
            print("A")
        total += num
    if fail>0:
        failed+=1
    else:
        pas+=1
    pe = total/5
    if hp < pe:
        hp = pe
    if lp > pe:
        lp = pe
print(f"""Number of passed students. : {pas}
Number of failed students. : {fail}
Highest percentage. : {hp}
Lowest percentage. : {lp}
""")