# 7. Python Program to Remove the Given Key from a Dictionary.

dict = {'name': 'Ganesh', 'age': 22, 'city': 'Tuljapur'}

key_to_remove = input("Enter the key to remove: ")

removed_value = dict.pop(key_to_remove, None)               # remove using pop()

if(removed_value is not None):
    print(f"Key '{key_to_remove}' removed with value {removed_value}.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

print("Updated dictionary:", dict)
