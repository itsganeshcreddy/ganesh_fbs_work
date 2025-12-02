# 8. Write a program to check whether a number is prime or not using recursion.

def is_prime(num, i=2):
    if(num <= 1):
        return False
    if(i == num):
        return True
    if(num % i == 0):
        return False
    return is_prime(num, i + 1)   

n = int(input("Enter a number: "))

# Calling function and printing result
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
