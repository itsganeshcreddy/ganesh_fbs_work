# 2. Python Program to Merge Two Lists and Sort it.

def merge_sort(li1, li2):
    merged = li1 + li2

    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if(merged[i] > merged[j]):
                merged[i], merged[j] = merged[j], merged[i]
    return merged

n1 = int(input("Enter how many element in first list? "))
li1 = []
for i in range(n1):
    li1.append(int(input(f"Enter element {i+1}: ")))

n2 = int(input("Enter how many element in second list? "))
li2 = []
for i in range(n2):
    li2.append(int(input(f"Enter element {i+1}: ")))

result = merge_sort(li1, li2)

print("First List:", li1)
print("Second List:", li2)
print("Merged & Sorted List:", result)    
