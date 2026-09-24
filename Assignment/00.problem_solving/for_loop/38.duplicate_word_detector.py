# Take a sentence.

# Find duplicate words.

# For each duplicate:

# Print the word.
# Print its frequency.
# Classify it as:
# "Repeated" → 2 times
# "Frequently Repeated" → 3–4 times
# "Highly Repeated" → more than 4 times
# Do not use count().
s = input("Enter a string to check : ").split()
dub=[]
rep=[]
hrep=[]
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count+=1
        if count == 2 and s[i] not in dub:
            dub.append(s[i])
        elif 2<count<=4 and s[i] not in rep:
            rep.append(s[i])
            if s[i] in rep:
                dub.remove(s[i])
        elif count>4 and (s[i] not in hrep):
            hrep.append(s[i])
            if s[i] in hrep:
                rep.remove(s[i])

print(f"{dub} is Repeated")
print(f"{rep} is Frequently repeated")
print(f"{hrep} is Highly repeated")