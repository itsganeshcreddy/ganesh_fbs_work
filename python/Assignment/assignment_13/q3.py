# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not.

dict = {'name': 'Ganesh', 'age': 22, 'city': 'Tuljapur'}
print(dict)

key = input("Enter the key to check: ")

if(key in dict):
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does not exist in the dictionary.")
