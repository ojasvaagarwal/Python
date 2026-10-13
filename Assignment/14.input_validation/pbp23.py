total = 0
for i in range(3):
    while True:
        score = int(input(f"Enter score {i + 1} (0-100): "))
        if 0 <= score <= 100:
            total += score
            break
        print("Score must be from 0 to 100")

print(f"Total: {total}")
print(f"Average: {total / 3}")
