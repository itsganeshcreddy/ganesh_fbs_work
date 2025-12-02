# 6. Python Program to Find the Union of two Lists.

def union_list(l1, l2):
    return list(set(l1 + l2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = union_list(list1, list2)
print("Union of lists:", result)