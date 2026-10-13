word = input("enter a word: ").strip()
count = 0

for ch in word:
    if ch in "aeiou":
        continue
    count += 1

print(count)
