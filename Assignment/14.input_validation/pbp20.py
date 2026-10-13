while True:
    count = int(input("How many numbers (1-20): "))
    if 1 <= count <= 20:
        break
    print("Enter a count from 1 to 20")

total = 0
for i in range(count):
    number = float(input("Enter a number: "))
    total += number

print(f"Average: {total / count}")
