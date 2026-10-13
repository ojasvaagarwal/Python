while True:
    n = int(input("""1. View profile
2. Edit profile
3. Settings
4. Exit
:"""))
    if n in (1,2,3,4):
        break
    print("invalid")
match n:
    case 1:
        print("Viewing profile")
    case 2:
        print("Editing profile")
    case 3:
        print("Opening settings")
    case 4:
        print("Exiting")