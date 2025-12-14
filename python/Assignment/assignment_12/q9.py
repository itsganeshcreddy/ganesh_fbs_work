# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String.and

text = input("Enter a string: ")

# Count characters (including spaces)
num_characters = 0
for char in text:
    num_characters += 1

# Count words by splitting string at spaces
words = text.split()
num_words = len(words)

print("Number of characters:", num_characters)
print("Number of words:", num_words)
