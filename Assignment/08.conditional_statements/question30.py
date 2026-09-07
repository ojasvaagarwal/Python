age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
has_id = input("Do you have an ID? (True/False): ") == "True"

if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")