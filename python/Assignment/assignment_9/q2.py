# 2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrong(num):
    if(num == 0):
        return 0
    return 1 + armstrong(num // 10)

def arm(num, count):
    if(num == 0):
        return 0
    return (num % 10) ** count + arm(num // 10, count)

num = int(input("Enter number:"))
count = armstrong(num)
result = arm(num, count)

if(num == result):
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrong number.')