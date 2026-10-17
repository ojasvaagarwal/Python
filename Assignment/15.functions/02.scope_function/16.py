def format_name(first, last, uppercase=False):
    if uppercase==True:return (first+" "+last).upper()
    return (first+" "+last)
print(format_name("Ojasva","Agarwal"))
print(format_name("Ojasva","Agarwal",True))