# 6. Python Program to Multiply All the Items in a Dictionary.

my_dict = {'a': 2, 'b': 3, 'c': 6}

product = 1

for value in my_dict.values():
    product *= value

print("Product of all items in the dictionary:", product)
