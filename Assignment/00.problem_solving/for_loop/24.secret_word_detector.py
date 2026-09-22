s = input("Enter a sentence : ").split()
w = input("Enter the secret word : ").strip()
count = 0
for i in range(len(s)):
    if s[i] == w:
        print(f"Secrect word '{w}' found first at {i}th position",end=" ")
        break
for i in range(len(s)):
    if s[i] == w:
        count+=1
print(f"and occured {count} times")