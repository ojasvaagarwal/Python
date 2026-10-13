nums = input("enter numbers: ").split()
target = input("enter target number: ").strip()

for i in nums:
    if i == target:
        print("Found")
        break
else:
    print("Not found")
