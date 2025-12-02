# 1. Python Program to Put Even and Odd elements of a List into two Different Lists.

def separate_even_odd(li):
    even_list = []
    odd_list = []
    
    for x in li:
        if(x % 2 == 0):
            even_list.append(x)
        else:
            odd_list.append(x)
    
    return even_list, odd_list

n = int(input("How many elements? "))
li = []

for i in range(n):
    li.append(int(input(f"Enter element {i+1}: ")))

even_list, odd_list = separate_even_odd(li)

print("Original List:", li)
print("Even List:", even_list)
print("Odd List:", odd_list)
