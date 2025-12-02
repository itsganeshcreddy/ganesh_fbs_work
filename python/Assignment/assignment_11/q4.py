# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.

def second_largest(li):
    n = len(li)

    # descending order
    for i in range(n):
        for j in range(0, n - i - 1):
            if(li[j] < li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]

    return li[1]   

li = [12, 45, 7, 23, 89, 56]

print("Original List:", li)
result = second_largest(li)
print("Second Largest Number:", result)
