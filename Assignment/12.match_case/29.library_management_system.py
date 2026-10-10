n = int(input("""1 → Search Book
2 → Issue Book
3 → Return Book
4 → View Issued Books
5 → Exit
Enter choice: """))
match n:
    case 1: print("Searching Books")
    case 2: print("Issuing Book")
    case 3: print("Returning Book")
    case 4: print("Opening Issued Books")
    case 5: print("Exit...")
    case _: print("Invalid Choice")
