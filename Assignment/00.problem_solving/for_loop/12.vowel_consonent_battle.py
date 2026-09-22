s = input("Enter a sentence : ")
vowel = 0
consonent = 0
for i in s:
    if i in "aeiouAeiou":
        vowel+=1
    if i in "qwrtyplkjhgfdszxcvbnmMNBVCXZSDFGHJKLPYTRWQ":
        consonent+=1
if vowel == consonent:    print("Draw")
elif vowel > consonent:    print("Vovel wins")
else:    print("consonent wins")