n = int(input("""1 → Start Game
2 → Load Game
3 → Settings
4 → Exit
Enter choice: """))
match n:
    case 1: print("Starting Game")
    case 2: print("Loading Game")
    case 3:
        m = int(input("""1 → Sound
2 → Graphics
3 → Controls
Enter setting: """))
        match m:
            case 1: print("Opening Sound Settings")
            case 2: print("Opening Graphics Settings")
            case 3: print("Opening Controls Settings")
            case _: print("Invalid Setting")
    case 4: print("Exit...")
    case _: print("Invalid Choice")
