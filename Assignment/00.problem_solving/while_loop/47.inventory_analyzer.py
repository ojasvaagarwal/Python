q0=q1=q2=q3=qh=0
p=""
for i in range(1,9):
    name = input("product name : ")
    q = int(input("product quantity : "))
    if q<0:
        print("invalid input")
    elif q==0:
        print(f"{name}, Out of stock")
        q0+=1
    elif q<6:
        print(f"{name}, Critical")
        q1+=1
    elif q<=20:
        print(f"{name}. Low")
        q2+=1
    else:
        print(f"{name}. Available")
        q3+=1
    if q>qh:
        qh=q
        p=name
print(f"""
"Out of Stock" - {q0}
"Critical" - {q1}
"Low" - {q2}
"Available" - {q3}
the product with the highest quantity is {p}
""")