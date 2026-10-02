sen = input("Enter a sentence : ").split()
wc=cc=lwl=0
swl=200
lw=sw=""
vw=wv=d=0
for i in sen:
    wc+=1
    c=0
    b=0
    for j in i:
        cc+=1
        c+=1
    if c>lwl:
        lwl=c
        lw=i
    if c<swl:
        swl=c
        sw=i
    if j in '1234567890':
        b+=1
    if i[0] in 'aeiouAEIOU':
        vw+=1
    if i[-1] in 'aeiouAEIOU':
        wv+=1
    if b>0:
        d+=1

print(f"""
Number of words. : {wc}
Number of characters. : {cc}
Longest word. : {lw}
Shortest word. : {sw}
Number of words beginning with a vowel. : {vw}
Number of words ending with a vowel. : {wv}
Number of words containing digits. : {d}
""")