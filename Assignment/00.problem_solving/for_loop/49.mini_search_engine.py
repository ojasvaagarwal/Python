l=[]
s=""
for j in range(1,11):
    sen = (input(f"Enter a sentence{j} : ").lower()).split()
    l+=sen
word = (input("Enter a secret word : ").lower()).strip()
c=0
for i in range(len(l)):
    c0=0
    for k in l[i]:
        if word == k:
            c0+=1
            c+=1
    print(f"in sentence{i}, word occured {c0} times")
print(f"the total number of occurrences across all sentences is {c}")