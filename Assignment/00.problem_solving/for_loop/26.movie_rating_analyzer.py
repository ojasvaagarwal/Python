poor =0
avg=0
good=0
exc=0
out=0
for i in range(1,11):
    rating = float(input(f"Rate movie{i} : "))
    if rating<0:
        print("invalid input")
    elif rating<=3:
        print("Poor")
        poor+=1
    elif rating<=5:
        print("Average")
        avg+=1
    elif rating<=7:
        print("Good")
        good+=1
    elif rating<=9:
        print("Excellent")
        exc+=1
    elif rating<=10:
        print("Outstanding")
        out+=1
print(f"""0–3 → "Poor" → {poor}
3.1–5 → "Average" → {avg}
5.1–7 → "Good" → {good}
7.1–9 → "Excellent" → {exc}
9.1–10 → "Outstanding → {out}""")