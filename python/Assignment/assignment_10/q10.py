# 10. Write a program to remove all occurrences of a given element in the list.

def remove_element(li, ele):
    new_list = []

    for x in li:
        if(x != ele):       # keep only elements that are NOT equal to ele
            new_list.append(x)
    return new_list


n = int(input("How many elements? "))
li = []

for i in range(n):
    li.append(int(input(f"Enter element {i+1}: ")))

ele = int(input("Enter the element to remove: "))

result = remove_element(li, ele)
print("Original List:", li)
print(f"List after removing {ele}:", result)
