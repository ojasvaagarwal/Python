s = input("Enter a sentence : ")
a = 0
ie = 0
e = 0
o = 0
u = 0
consonent = 0
for i in s:
    if i in "aA":
        a+=1
    elif i in "eE":
        e+=1
    elif i in "iI":
        ie+=1
    elif i in "oO":
        o+=1
    elif i in "uU":
        u+=1
    elif i in "qwrtyplkjhgfdszxcvbnmMNBVCXZSDFGHJKLPYTRWQ":
        consonent+=1
vowel = a+ie+e+o+u
if vowel == consonent:    print("Draw")
elif vowel > consonent:    print("Vovel wins")
else:    print("consonent wins")
print(f"Frequency of each vowel :-\n\t a : {a}\n\t e : {e}\n\t i : {ie}\n\t o : {o}\n\t u : {u}")