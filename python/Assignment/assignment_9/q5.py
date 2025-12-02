# 5. Write a program to find factorial using recursion. 

def fact(n):
    if(n == 1 or n == 0):     # base condition
        return 1
    return n * fact(n - 1)

n = int(input("Enter number: "))
result = fact(n)
print("Factorial =", result)
