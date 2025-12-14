# 2. Python Program to Remove the nth Index Character from a Non-Empty String.

text = input("Enter a string: ")
n = int(input("Enter index to remove: "))

# Remove nth character
new_text = text[:n] + text[n+1:]

print("Modified string:", new_text)
