# 6. Write a program to remove duplicates from the list.

def remove_duplicates(li):
    unique = []

    for x in li:
        if(x not in unique):   # allowed (not a function)
            unique.append(x)
    return unique

n = int(input("How many elements? "))
li = []

for i in range(n):
    li.append(int(input()))

result = remove_duplicates(li)
print("List after removing duplicates:", result)
