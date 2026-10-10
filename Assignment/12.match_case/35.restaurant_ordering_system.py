n = int(input("""1 → Starters
2 → Main Course
3 → Desserts
4 → Drinks
Enter category: """))
match n:
    case 1:
        m = int(input("""1 → Soup
2 → Spring Roll
3 → Garlic Bread
Enter item: """))
        match m:
            case 1: print("Soup Selected")
            case 2: print("Spring Roll Selected")
            case 3: print("Garlic Bread Selected")
            case _: print("Invalid Item")
    case 2:
        m = int(input("""1 → Pizza
2 → Pasta
3 → Biryani
Enter item: """))
        match m:
            case 1: print("Pizza Selected")
            case 2: print("Pasta Selected")
            case 3: print("Biryani Selected")
            case _: print("Invalid Item")
    case 3:
        m = int(input("""1 → Ice Cream
2 → Cake
3 → Gulab Jamun
Enter item: """))
        match m:
            case 1: print("Ice Cream Selected")
            case 2: print("Cake Selected")
            case 3: print("Gulab Jamun Selected")
            case _: print("Invalid Item")
    case 4:
        m = int(input("""1 → Coffee
2 → Tea
3 → Juice
Enter item: """))
        match m:
            case 1: print("Coffee Selected")
            case 2: print("Tea Selected")
            case 3: print("Juice Selected")
            case _: print("Invalid Item")
    case _: print("Invalid Category")
