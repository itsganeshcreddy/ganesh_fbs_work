# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

def duplicate_list(li):
    new_list = []

    for x in li:
        new_list.append(x)
    return new_list

n = int(input("Enter how many elements? "))
li = []

for i in range(n):
    li.append(int(input()))

result = duplicate_list(li)
print("Original list:", li)    
print("Duplicate list:", result)    