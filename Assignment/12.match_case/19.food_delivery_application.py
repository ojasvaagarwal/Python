n = int(input("""1 → Vegetarian
2 → Non-Vegetarian
Enter category: """))
match n:
    case 1:
        m = int(input("""1 → Paneer
2 → Dal
3 → Veg Biryani
Enter food: """))
        match m:
            case 1: print("Paneer Selected")
            case 2: print("Dal Selected")
            case 3: print("Veg Biryani Selected")
            case _: print("Invalid Food")
    case 2:
        m = int(input("""1 → Chicken Biryani
2 → Chicken Curry
3 → Fish Fry
Enter food: """))
        match m:
            case 1: print("Chicken Biryani Selected")
            case 2: print("Chicken Curry Selected")
            case 3: print("Fish Fry Selected")
            case _: print("Invalid Food")
    case _: print("Invalid Category")
