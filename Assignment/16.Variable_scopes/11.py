def make_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter
count_up=make_counter()
print(count_up())
print(count_up())
print(count_up())
