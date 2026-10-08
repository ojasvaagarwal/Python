n = int(input("""1 → Wi-Fi
2 → Bluetooth
3 → Mobile Data
4 → Airplane Mode
5 → Exit
:"""))
match n:
    case 1:
        print("Selected Wi-Fi")
    case 2:
        print("Selected Bluetooth")
    case 3:
        print("Selected Mobile Data")
    case 4:
        print("Selected Airplane Mode")
    case 5:
        print("Exit...")
    case _:
        print("Invalid Setting")