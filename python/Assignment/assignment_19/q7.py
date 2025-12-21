# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit. 

res = [i for i in range(1, 1001) for k in range(1, 10) if(i % k == 0)]
print(res)

# nums_div_any = [x for x in range(1, 1001) if any(x % d == 0 for d in range(1, 10))]
# print(nums_div_any)
