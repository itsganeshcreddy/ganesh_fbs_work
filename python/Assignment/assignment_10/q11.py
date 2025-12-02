# 11.Write a program to print all numbers which are divisible by m and n in the list.

def div_by_m_n(li, m, n):
    result = []
    for x in li:
        if(x % m == 0 and x % n == 0):  # check divisibility by both m and n
            result.append(x)
    return result


# Main program
n_ele = int(input("How many elements? "))
li = []

for i in range(n_ele):
    li.append(int(input(f"Enter element {i+1}: ")))

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

result = div_by_m_n(li, m, n)

print("Original List:", li)
print(f"Numbers divisible by {m} and {n}:", result)

