sc=dc=bv=bd=0
s = input("Enter a string : ")
for i in range(len(s)):
    for j in range(i,len(s)):
        if i!=j:
            if s[i] == s[j]:
                sc+=1
            else :
                dc+=1
            if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                bv+=1
            if s[i] in "0123654789" and s[j] in "0123654789":
                bd+=1

print(f"""
Same characters : {sc}
Different characters : {dc}
Both vowels : {bv}
Both digits : {bd}
""")