def multi(a):
    def multiply(n):
        return n*a
    return multiply
x2=multi(2)
x3=multi(3)
print(x2(5))
print(x3(5))

# Explanation:
# The variable a from multi remains available inside multiply even after multi finishes running.
# This happens because multiply is a closure: it remembers the enclosing scope variable (a) that it references.
