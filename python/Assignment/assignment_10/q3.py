# 3. Write a program to find the second largest element in the list.

def smaxEle(li):
    max = li[0]
    smax = 0
    for ind in range(len(li)):
        if(li[ind] > max):
            smax = max
            max = li[ind]
        elif(li[ind] > smax):
            smax = li[ind]
    return smax

li = [30, 20, 80, 60]
print(smaxEle(li))