# 8. Python Program to Remove the Characters of Odd Index Values in a String.

text = input("Enter a string: ")

# only characters at even (0, 2, 4, ...)
new_text = text[::2]

print("Modified string:", new_text)
