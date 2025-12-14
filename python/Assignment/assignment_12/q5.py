# 5. Python Program to Count the Number of Vowels in a String.

text = input("Enter a string: ")

text = text.lower()

count = 0

for char in text:
    if(char in "aeiou"):
        count += 1

print("Number of vowels:", count)
