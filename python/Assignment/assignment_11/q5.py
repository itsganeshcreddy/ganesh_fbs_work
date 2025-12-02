# 5. Python Program to Sort a List According to the Length of the Elements within the list.

def sort_by_length(li):

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if(len(li[i]) > len(li[j])):
                li[i], li[j] = li[j], li[i]
    return li

li = ["Ganesh", "Gopal", "Nivrutti", "Rahul", "Omkar"]

print("Original List:", li)
result = sort_by_length(li)
print("Sorted List by Length:", result)
