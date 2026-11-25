# Why avoid variable names like list, str, and sum:
# In Python, list, str, and sum are built-in names (in the built-in scope).
# If you assign a value to a variable named list, str, or sum, it shadows (hides) the built-in function/type in that scope.
# After that, calling list(), str(), or sum() will raise a TypeError because the name now refers to your variable instead of the built-in.
