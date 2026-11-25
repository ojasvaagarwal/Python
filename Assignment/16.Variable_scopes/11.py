def make_counter():
    count=0
    def inc():
        nonlocal count
        count+=1
        return count
    return inc
counter=make_counter()
print(counter())
print(counter())
print(counter())
