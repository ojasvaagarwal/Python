pin = "2468"
attempts = 0
correct = False

while attempts < 3 and correct == False:
    entered_pin = input("Enter PIN: ")
    attempts += 1
    if entered_pin == pin:
        print("Access granted")
        correct = True

if correct == False:
    print("Access denied")
