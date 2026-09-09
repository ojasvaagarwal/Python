char = input("Enter the character : ")
length = len(char)

if length == 1:
    if char >= chr(97) and char <= chr(123):
        print("Lowercase alphabet")
    elif char >= chr(65) and char <= chr(90):
        print("Uppercase alphabet")
    elif char >= chr(48) and char <= chr(57):
        print("Digit")
    else:
        print("Special Charater")
else:
    print("Invalid")