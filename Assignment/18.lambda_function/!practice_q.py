# Create a lambda function to multiply two numbers.

multi = lambda a,b:a*b
print(multi(2,3))

# Create a lambda function to calculate the cube of a number.

cube = lambda a:a*a*a
print(cube(3))

# Create a lambda function to check whether a number is positive or negative.

p_n = lambda n:"Positive" if n>=0 else "Negative"
print(p_n(7))

# Create a lambda function to find the smaller of two numbers.

lt = lambda a,b:a if a>b else b
print(lt(3,4))

# Create a lambda function to calculate the area of a rectangle.

ar_rct = lambda l,b: l*b
print(ar_rct(10,20))

# Create a lambda function to convert a string into lowercase.

lwcs = lambda s: s.lower()
print(lwcs("PytHon"))

# Create a lambda function to check whether a character is a vowel.

f_vwl = lambda s: s in "aeiou"
print(f_vwl("i"))

# Use map() and lambda to convert every character of "coding" into uppercase.

a = map(lambda i:i.upper(),"coding")
print("".join(a))

# Use filter() and lambda to extract vowels from "programming".

a = filter(lambda i:f_vwl(i),"programming")
print("".join(a))
