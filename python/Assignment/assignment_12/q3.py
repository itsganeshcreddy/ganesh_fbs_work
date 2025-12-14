# 3. Python Program to Detect if Two Strings are Anagrams.

# Input two strings from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase for accurate comparison
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if sorted characters of both strings are equal
if(sorted(str1) == sorted(str2)):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
