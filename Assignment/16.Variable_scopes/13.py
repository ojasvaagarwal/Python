x=100
squares=[x*x for x in range(1,4)]
print(x)

for x in range(1,4):
    pass
print(x)

# Explanation:
# A normal for loop does not create its own scope, so its loop variable lives in the enclosing/current scope and stays available (and overwrites x) after the loop ends.
# In Python 3, a list comprehension runs in its own separate scope, so its loop variable exists only inside the comprehension and does not overwrite the outer x.
