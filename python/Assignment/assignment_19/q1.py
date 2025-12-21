# 1. Find all of the numbers from 1–1000 that are divisible by 8

num = [n for n in range(1, 1001) if(n % 8 == 0)]
print(num)