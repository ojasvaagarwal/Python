print("write a sentence :")
a=str(input())
print(a)  # The original sentence.
print(len(a))  # Number of characters.
print(len(a.split()))  # Number of words.
print(a[0])  # First character.
print(a[-1])  # Last character.
print(a.upper())  # Sentence in uppercase.
print(a.lower())  # Sentence in lowercase.
print(a.title())  # Sentence in title case.
print(a.find("Python"))  # Whether "Python" exists in the sentence.
print(a.count("a"))  # Number of times a chosen character occurs.