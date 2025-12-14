# 4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value. 

def find_pairs(numbers, target_sum):
    seen = set()                                   # store visited numbers
    pairs = set()    

    for num in numbers:
        diff = target_sum - num                      # number we need

        if(diff in seen):                            # check if pair exists
            pairs.add(tuple(sorted((num, diff))))

        seen.add(num)

    return pairs

numbers = [2, 4, 3, 5, 7, 8, 9]
target = int(input("Enter Target sum:"))

result = find_pairs(numbers, target)
print("Pairs:", result)


