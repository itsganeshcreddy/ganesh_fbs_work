# 6. Write a Python program to find the two numbers whose product is maximum 
#     among all the pairs in a given list of numbers. Use the Python set.

def max_product_pair(numbers):
    nums = list(set(numbers))   # remove duplicates using set
    nums.sort()                 # sort numbers

    # 1) two largest numbers
    # 2) two smallest (negative * negative = positive)

    prod1 = nums[-1] * nums[-2]       # largest two
    prod2 = nums[0] * nums[1]         # smallest two

    if(prod1 > prod2):
        return nums[-1], nums[-2], prod1
    else:
        return nums[0], nums[1], prod2
    
nums = list(map(int, input("Enter numbers: ").split()))

a, b, product = max_product_pair(nums)
print("Numbers:", a, "and", b)
print("Maximum Product:", product)
