for I in range(1,11):
    highest_score=most_vowel=most_digits=0
    s = input(f"Enter string{I} : ")
    count_uppercase_letters = 0
    count_lowercase_letters = 0
    count_digits = 0
    count_spaces = 0
    count_special_characters = 0
    vowel=0
    consonent = 0
    word=""
    high_s = 0
    rc=0
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
        score = 0
        for j in s:
            if j in "aeiouAEIOU":
                score+=2
                vowel+=1
            elif j in "qwrtypsdfghjklzxcvbnmQWRTYPLKJHGFDSZXCVBNM":
                score+=1
                consonent+=1
            elif j >= chr(48) and i <= chr(57):
                score+=3
            elif j == " ":
                score+=0
            else:
                score+=4
        if score > high_s:
            high_s = score
            word = j
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j:    
                    if s[i]==s[j]:
                        rc+=1
    if vowel > most_vowel:
        most_vowel = vowel
        most_vowel0 = s
    print(f"""
Count uppercase letters. {count_uppercase_letters}
Count lowercase letters. {count_lowercase_letters}
Count vowels. {vowel}
Count consonants. {consonent}
Count digits. {count_digits}
Count spaces. {count_spaces}
Count special characters. {count_special_characters}
Find the longest word. {word}
Find the number of repeated characters. {rc/2}  
Score. {score}
""")