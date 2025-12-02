# 7. Python Program to Find the Intersection of Two Lists.

def intersection_list(l1, l2):
    return list(set(l1) & set(l2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = intersection_list(list1, list2)
print("Intersection:", result)
