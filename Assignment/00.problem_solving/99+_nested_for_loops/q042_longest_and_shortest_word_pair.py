s = input("enter a sentence: ").split()
l=99999999
h=0
for i in s:
    if len(i)>h:
        hw=i
        h=len(i)
    if len(i)<l:
        lw=i
        l=len(i)
print(f"longest = {hw}\nshortest = {lw}")