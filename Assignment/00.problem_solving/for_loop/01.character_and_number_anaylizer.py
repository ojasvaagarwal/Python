s = input("Enter a string : ")
count_uppercase_letters = 0
count_lowercase_letters = 0
count_digits = 0
count_spaces = 0
count_special_characters = 0

for i in s:
    if i >= 'a' and i <= 'z':
        count_lowercase_letters+=1
    elif i >= 'A' and i <= 'Z':
        count_uppercase_letters+=1
    elif i >= chr(48) and i <= chr(57):
        count_digits+=1
    elif i == ' ':
        count_spaces+=1
    else:
        count_special_characters+=1

if count_spaces > count_digits and count_spaces > count_special_characters and count_spaces > count_uppercase_letters and count_spaces > count_lowercase_letters :
    print(f"Spaces have highest count {count_spaces}")
elif count_uppercase_letters > count_digits and count_uppercase_letters > count_special_characters and count_uppercase_letters > count_spaces and count_uppercase_letters > count_lowercase_letters :
    print(f"Uppercase letters have highest count {count_uppercase_letters}")
elif count_lowercase_letters > count_digits and count_lowercase_letters > count_special_characters and count_lowercase_letters > count_uppercase_letters and count_lowercase_letters > count_spaces :
    print(f"Lowercase lettters have highest count {count_lowercase_letters}")
elif count_special_characters > count_digits and count_special_characters > count_spaces and count_special_characters > count_uppercase_letters and count_special_characters > count_lowercase_letters :
    print(f"Special charaters have highest count {count_special_characters}")
elif count_digits > count_spaces and count_digits > count_special_characters and count_digits > count_uppercase_letters and count_digits > count_lowercase_letters :
    print(f"Digits have highest count {count_digits}")
else:
    print("tie among diffent catogries")