highest = 0
for i in range(1,6):
    name = input(f"Enter student{i} name : ")
    num = int(input(f"Enter marks for student{i} : "))
    if num < 0 or num > 100:
        print("invalid input")
        break
    elif num < 35:
        print("Fail")
    elif num <= 60:
        print("C Grade")
    elif num <= 80:
        print("B Grade")
    else:
        print("A Grade")
    vowel = 0
    consonent = 0
    char=0
    for j in name:
        char+=1
        if j in "aeiouAeiou":
            vowel+=1
        if j in "qwrtyplkjhgfdszxcvbnmMNBVCXZSDFGHJKLPYTRWQ":
            consonent+=1
    print(f"Vowels in name are : {vowel}")
    print(f"characters in name : {char}")
    if vowel == consonent:    print("Balanced name")
    elif vowel > consonent:    print("Vovels are more in name")
    else:    print("consonents more in name\n")
    if num > highest:
        highest = num
        std = name
print(f"\n\t{std} scored highest")