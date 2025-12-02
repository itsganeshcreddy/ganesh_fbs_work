# 7. Write a program to create a new list from existing list which contains cube of each number of list.

def cube_list(li):
    new_list = []

    for x in li:
        new_list.append(x * x * x)

    return new_list

n = int(input("How many element? "))
li = []

for i in range(n):
    li.append(int(input()))

result = cube_list(li)
print("Original list:", li)
print("List with cube:", result)    