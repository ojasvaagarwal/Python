def count_digits(number):
    number = abs(number)
    count=0
    while number>0:
        count+=1
        number=number//10
    return count
print(count_digits(26347824))
