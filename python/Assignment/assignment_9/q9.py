# 9. Write a program to calculate the m to the power n using recursion. 

def power(m, n):
    if(n == 0):
        return 1          # anything raised to 0 is 1
    else:
        return m * power(m, n - 1)   # recursive formula

m = int(input("Enter the base (m): "))
n = int(input("Enter the power (n): "))

result = power(m, n)
print(f"{m} to the power {n} is {result}")
