nums = input("enter numbers: ").split()

for i in nums:
    if i == "0":
        continue
    if i == "-1":
        break
    print(i)
else:
    print("All values processed")
