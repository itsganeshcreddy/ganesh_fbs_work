# 2. Write a program to find maximum and minimum element in a list.

# maximum element of list...

def maxEle(li):
    max = li[0]
    for ind in range(0, len(li)):
        if(max < li[ind]):
            max = li[ind]
    return max
        
li = [34, 65, 23, 56, 89]
max_el  = maxEle(li)
print("Maximum element of list is:",max_el)


# minimum element of list...

def minEle(li):
    min = li[0]
    for ind in range(len(li)):
        if(min > li[ind]):
            min = li[ind]
    return min 

li = [60,5,20,10,50]
min_el = minEle(li)
print("Minimum element of list is:",min_el)        

