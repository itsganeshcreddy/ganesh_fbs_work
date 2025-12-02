# 1. Write a program to find sum of all elements of list

def sumOfEle(li):
    sum = 0
    for ind in range(0, len(li)):
        sum = sum + li[ind]
    return sum
        
li = [10 ,20, 30, 40, 50]
result = sumOfEle(li)
print(result)