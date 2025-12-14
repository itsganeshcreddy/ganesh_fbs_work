# 12.  Python Program to count number of lowercase characters in a string. 

text = input("Enter a string: ")

count = 0

for char in text:
    if char.islower():
        count += 1

print("Lowercase characters:", count)
