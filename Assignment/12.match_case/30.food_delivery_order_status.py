status = input("Enter status: ").strip().lower()
match status:
    case "placed": print("Your order has been placed")
    case "confirmed": print("Your order is confirmed")
    case "preparing": print("Your order is being prepared")
    case "out_for_delivery": print("Your order is on the way")
    case "delivered": print("Your order has been delivered")
    case "cancelled": print("Your order was cancelled")
    case _: print("Unknown Order Status")
