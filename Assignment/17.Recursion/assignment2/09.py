def og_dg(n):
    if n=="":return True
    if not("0"<=n[0]<="9"):return False
    return og_dg(n[1:])

print(og_dg("12345"))
print(og_dg("123r5"))
print(og_dg("1235r"))
print(og_dg("w1235"))