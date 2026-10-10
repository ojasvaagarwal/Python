n = input("""sunny
rainy
cloudy
snowy
Exit
Enter weather:"""))
match n:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case "Exit":
        print("Exit...")
    case _:
        print("Unknown Weather")
