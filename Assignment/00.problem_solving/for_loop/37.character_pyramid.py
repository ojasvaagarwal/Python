word = input("Enter a word : ").strip()
for i in range(len(word)):
    for j in range(i+1):
        print(word[j],end="")
    print()
# word=word[::-1] can be used here to get string reverced.
for i in range(len(word)):
    for j in range(len(word)-i):
        print(word[j],end="")
    print()