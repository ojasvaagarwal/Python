op=int(input("OPERATIONS\n\t1.Addition\n\t2.Subtraction\n\t3.Multiply\n\t4.Divide\nEnter the associated number to choose : "))
if op==1 or op==2 or op==3 or op==4:
    x=int(input("Enter number 1 : "))
    y=int(input("Enter number 2 : "))
    if op == 1:
        print("Addition is :",x+y)
    elif op == 2:
        print("Subtraction is :",x-y)
    elif op == 3:
        print("Multiple is :",x*y)
    elif op == 4:
        if y == 0:
            print("Division is :","infinity")
        else:
            print("Division is :",x/y)
else:
    print("Wrong choice")