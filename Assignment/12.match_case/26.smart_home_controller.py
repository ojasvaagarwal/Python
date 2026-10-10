n = int(input("""1 → Light
2 → Fan
3 → AC
4 → TV
Enter device: """))
match n:
    case 1: print("Light Controller Opened")
    case 2: print("Fan Controller Opened")
    case 3: print("AC Controller Opened")
    case 4: print("TV Controller Opened")
    case _: print("Invalid Device")
