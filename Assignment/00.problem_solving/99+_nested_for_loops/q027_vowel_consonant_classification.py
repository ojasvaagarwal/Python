s = input("enter a number: ").lower()
for i in s:
    if i in "aeiou":
        print(i,"= vowel")
    if i in "qwrtyplkjhgfdszxcvbnm":
        print(i,"= consonent")