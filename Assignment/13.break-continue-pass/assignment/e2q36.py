nums = input("enter numbers: ").split()
target = input("enter target number: ").strip()

for i in nums:
    if int(i) < 0:
        continue
    if i == target:
        print("Target found")
        break
else:
    print("Target not found")
