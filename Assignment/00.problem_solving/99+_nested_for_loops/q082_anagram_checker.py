s1 = input("enter word1: ").strip()
s2 = input("enter word2: ").strip()
if len(s1)==len(s2):
    s01 = {}
    s02 = {}
    for i in range(len(s1)):
        s01[s1[i]]=0
        s02[s2[i]]=0
    for i in s1:
        s01[i]+=1
    for i in s2:
        s02[i]+=1

    if s01==s02:print("Anagram")
    else:print("Not Anagram")
else:print("Not Anagram")