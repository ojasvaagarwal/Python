def convert_temperature(value, scale="C"):
    if scale=="F":return (value*9/5)
    return (value-32)*5/9
print(convert_temperature(33))
print(convert_temperature(98,"F"))