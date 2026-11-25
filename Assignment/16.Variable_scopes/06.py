value = 100
def test():
    value = 200
    print(value)
test()
print(value)

# output
# 200
# 100
# test() creates a new local variable named value (200), so the global value (100) stays unchanged.
