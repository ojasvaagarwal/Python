nums = input("enter numbers: ").split()
for i in nums:
    number = int(i)
    if number < 0:
        continue
    if number % 4 == 0 and number % 6 == 0:
        print("Found:", number)
        break
else:
    print("No matching number")