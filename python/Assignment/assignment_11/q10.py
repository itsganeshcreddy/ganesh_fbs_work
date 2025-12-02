# 10. Write a program to print list after removing even numbers.

def remove_even(li):
    new_list = []
    for x in li:
        if(x % 2 != 0):   # only odd numbers
            new_list.append(x)
    return new_list

n = int(input("How many elements? "))
li = []

for i in range(n):
    li.append(int(input(f"Enter element {i+1}: ")))

result = remove_even(li)

print("Original List:", li)
print("List after removing even numbers:", result)
