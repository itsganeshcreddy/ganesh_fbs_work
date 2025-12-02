# 3. Python Program to Sort the List According to the Second Element in Sublist.

def sort_by_second(li):
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i][1] > li[j][1]:
                li[i], li[j] = li[j], li[i]
    return li

li = [[2, 5], [1, 3], [4, 1], [6, 2]]

print("Original List:", li)
result = sort_by_second(li)
print("Sorted List:", result)
