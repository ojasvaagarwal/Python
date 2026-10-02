s = input("Enter a sentence : ").split()
for i in s:
    vowel = 0
    consonent = 0
    for j in i:
        if i in "aeiouAeiou":
            vowel+=1
        if i in "qwrtyplkjhgfdszxcvbnmMNBVCXZSDFGHJKLPYTRWQ":
            consonent+=1
    if vowel == consonent:    print(i,"Balanced")
    elif vowel > consonent:    print(i,"Vovel Heavy")
    else:    print(i,"consonent Heavy")