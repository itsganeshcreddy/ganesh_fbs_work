# 4. Write a program to reverse the list.

def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while(start < end):
        (lst[start]), (lst[end]) = (lst[end]), (lst[start])
        start = start + 1 
        end = end - 1
    return lst

li = [10, 20, 30, 40, 50] 
result = (reverse_list(li))
print("Reverse list:",result)   
