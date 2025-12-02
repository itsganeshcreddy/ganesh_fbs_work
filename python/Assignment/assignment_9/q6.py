# 6. Write a program to print Fibonacci series using recursion.

def fib(n):
    if(n == 0):
        return 0         
    elif(n == 1):
        return 1         
    else:
        return fib(n-1) + fib(n-2) 

terms = int(input("Enter how many terms you want: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fib(i), end=" ")
