# # 5. Accept a number from user and check if this element is present in the list or 
# #    not. Also tell how many times it is present in the list.

def check_ele(lst, num):
    count = 0

    for item in lst:
        if(item == num):
            count = count + 1
    return count

li = [10, 20, 30, 20, 40, 30, 50, 60, 40, 30, 30]
n = int(input("Enter number for check:"))
result = check_ele(li, n)

if result > 0:
    print(f"{n} is present in list.")
    print(f"it appears {result} times")
else:
    print(f"{n} is not present in list.")  

