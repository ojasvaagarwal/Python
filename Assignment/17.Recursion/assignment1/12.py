def reverse_text(s):
    if s=="":return ""
    return reverse_text(s[1:]) + s[0]



print(reverse_text("cat"))  # "tac"
print(reverse_text("a"))    # "a"
print(reverse_text(""))     # ""