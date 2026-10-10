n = input("""upi
card
cash
wallet
Enter payment method:"""))
match n:
    case "upi":
        print("UPI Payment Selected")
    case "card":
        print("card Payment Selected")
    case "cash":
        print("cash Payment Selected")
    case "wallet":
        print("wallet Payment Selected")
    case _:
        print("Payment canceled")
