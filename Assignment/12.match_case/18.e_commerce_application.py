n = int(input("""1 → Electronics
2 → Clothing
Enter category: """))
match n:
    case 1:
        m = int(input("""1 → Mobile
2 → Laptop
3 → Headphones
Enter product: """))
        match m:
            case 1: print("Mobile Selected")
            case 2: print("Laptop Selected")
            case 3: print("Headphones Selected")
            case _: print("Invalid Product")
    case 2:
        m = int(input("""1 → Shirt
2 → Jeans
3 → Shoes
Enter product: """))
        match m:
            case 1: print("Shirt Selected")
            case 2: print("Jeans Selected")
            case 3: print("Shoes Selected")
            case _: print("Invalid Product")
    case _: print("Invalid Category")
