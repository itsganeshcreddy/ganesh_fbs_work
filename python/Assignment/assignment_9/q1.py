# 1. Write a program to find sum of following series using recursive functions:i. 1! + 2!  + 3! + 4! +….. + n!  
#      Note : For fact and sum two recursive functions 

def fact(num):
    if(num == 1):
        return 1
    return num * fact(num - 1)

# Recursive function to find sum of factorial series
def sum_series(n):
    if(n == 1):
        return 1
    return fact(n) + sum_series(n - 1)

n = int(input("Enter value of n: "))
result = sum_series(n)
print("Sum of series =", result)
