sentence =  input("enter a sentence: ").split()
tw = input("enter target word: ").strip()

for i in sentence:
    if i == tw:
        print("found")
        break
else:print("not found")