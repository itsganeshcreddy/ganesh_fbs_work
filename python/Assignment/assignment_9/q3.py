# 3. Write a program to reverse a given number using recursive function.

def reverse(num, rev=0):
    if(num == 0):
        return rev
    rev = rev * 10 + (num % 10)
    return reverse(num // 10, rev)

n = int(input("Enter number: "))
result = reverse(n)
print("Reversed number =", result)
