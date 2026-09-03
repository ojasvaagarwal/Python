first_name = input().strip()
last_name = input().strip()
city = input().strip()
course = input().strip()
age = input().strip()

# 2. Create the full name
full_name = f"{first_name} {last_name}"
# 3. Display the full name in title case
print(full_name.title())
# 4. Display the full name in uppercase
print(full_name.upper())
# 5. Display the full name in lowercase
print(full_name.lower())
# 6. Display the length of the full name
print(len(full_name))
# 7. Display the first character of the full name
if full_name:
    print(f"First character: {full_name[0]}")
# 8. Display the last character of the full name
if full_name:
    print(f"Last character: {full_name[-1]}")
# 9. Display the city and course
print(f"City: {city.title()} | Course: {course.title()}")
# 10. Display the age using an f-string
print(f"You are {age} years old.")
# 11. Check whether the course contains "Python"
# Using .lower() to ensure the check is case-insensitive
contains_python = "python" in course.lower()
print(f"Course contains 'Python': {contains_python}")
# 12. Replace one word in the course name with another word
print("\n--- Modify Course Name ---")
old_word = input(f"Enter a word from '{course}' you want to replace: ").strip()
new_word = input("Enter the new word: ").strip()

modified_course = course.replace(old_word, new_word)
print(f"Modified Course Name: {modified_course}")
# 13. Display the number of words in the course name
# .split() separates the string into a list by spaces
word_count = len(course.split())
print(f"Number of words in original course name: {word_count}")