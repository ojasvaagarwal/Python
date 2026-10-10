n = int(input("""1 → Engine
2 → Lights
3 → Music
4 → Navigation
Enter option: """))
match n:
    case 1:
        m = int(input("""1 → Start
2 → Stop
Enter engine option: """))
        match m:
            case 1: print("Engine Started")
            case 2: print("Engine Stopped")
            case _: print("Invalid Engine Option")
    case 2:
        m = int(input("""1 → Headlights
2 → Indicators
3 → Hazard Lights
Enter light option: """))
        match m:
            case 1: print("Headlights Selected")
            case 2: print("Indicators Selected")
            case 3: print("Hazard Lights Selected")
            case _: print("Invalid Light Option")
    case 3:
        m = int(input("""1 → Play
2 → Pause
3 → Next
4 → Previous
Enter music option: """))
        match m:
            case 1: print("Music Playing")
            case 2: print("Music Paused")
            case 3: print("Next Track")
            case 4: print("Previous Track")
            case _: print("Invalid Music Option")
    case 4:
        m = int(input("""1 → Start Navigation
2 → Stop Navigation
Enter navigation option: """))
        match m:
            case 1: print("Navigation Started")
            case 2: print("Navigation Stopped")
            case _: print("Invalid Navigation Option")
    case _: print("Invalid Option")
