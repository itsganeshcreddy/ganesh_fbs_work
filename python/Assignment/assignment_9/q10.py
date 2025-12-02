# 10. Write a program to reverse a number using recursion.

def reverse_number(num):
    if num < 10:          # base case: single digit
        return str(num)
    else:
        return str(num % 10) + reverse_number(num // 10)

n = int(input("Enter a number: "))

result = reverse_number(n)
print("Reversed number:", result)


