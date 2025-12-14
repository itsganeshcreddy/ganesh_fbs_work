# 7. Given two sets of numbers, write a Python program to find the missing numbers in the second set
#     as compared to the first and vice versa. Use the Python set.

def find_missing_numbers(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1

    return missing_in_set2, missing_in_set1

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 7}

missing2, missing1 = find_missing_numbers(set1, set2)

print("Missing in Set 1:", missing1)
print("Missing in Set 2:", missing2)
