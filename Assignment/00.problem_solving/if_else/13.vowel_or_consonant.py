char = input("Enter the character : ")
length = len(char)

vowel = "aeiouAEIOU"
consonent = "qwrtypsdfghjKlzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

if length == 1:
    if char in vowel:
        print("Vowel")
    elif char in consonent:
        print("Consonent")
    else:
        print("Invalid input")
else:
    print("Invalid input")