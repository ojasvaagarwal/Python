def analyze_number(number):
    if number<0:number*=-1
    number0=number
    if number%2==0:even="is even"
    else:even="not even"
    count=0
    while number>0:
        count+=1
        number=number//10
    return number0,even,count
print(analyze_number(-89))