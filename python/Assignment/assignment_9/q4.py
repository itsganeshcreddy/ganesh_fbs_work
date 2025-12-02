# 4. Write a program to find sum of n numbers using recursion. 

def sumN(n):
    if(n == 1):
        return 1
    return n + sumN(n - 1)

n = int(input("Enter value of n: "))
result = sumN(n)
print("Sum =", result)
