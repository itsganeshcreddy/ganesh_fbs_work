# 9. Write a program of having n number of elements in the list and find out even 
#    and odd elements in that list and then create two separate lists which will have 
#    even elements and other will have odd elements.

def sep_even_odd(li):
    even_list = []
    odd_list = []

    for x in li:
        if(x % 2 == 0):
            even_list.append(x)
        else:
            odd_list.append(x)
    return even_list, odd_list

n = int(input("Enter how many elements? "))
li = []

for i in range(n):
    li.append(int(input(f"Enter element {i+1}: ")))

even_list, odd_list = sep_even_odd(li)

print("Original List:", li)
print("Even Elements List:", even_list)
print("Odd Elements List:", odd_list)