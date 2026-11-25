x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)
outer()
print(x)

# output
# 3
# 2
# 1
# Each function defines its own local x, so inner() prints 3, outer() prints 2, and global prints 1.
