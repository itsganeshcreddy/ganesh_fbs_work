# 7. Write a program to find sum of digits using recursion.

def sum_digits(num):
    if(num <= 0):
        return 0
    else:
        return (num % 10) + sum_digits(num // 10)

n = int(input("Enter a number: "))
result = sum_digits(n)
print("Sum of digits:", result)

