def make_multiplier(factor):
    def multiply(number):
        return number*factor
    return multiply
double=make_multiplier(2)
print(double(5))

# Explanation:
# The variable factor from make_multiplier remains available inside multiply even after make_multiplier finishes running.
# This happens because multiply is a closure: it remembers the enclosing scope variable (factor) that it references.
