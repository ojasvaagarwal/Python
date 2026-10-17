def classify_number(number):
    if number<0:return "Negative"
    if number==0:return "Zero"
    return "Positive"
print(classify_number(8293))
print(classify_number(0))
print(classify_number(-28823))