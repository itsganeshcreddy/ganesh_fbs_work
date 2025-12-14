# 9. Write a Python program to find all the unique combinations of  
#     3 numbers from a given list of numbers, adding up to a target number.

def three_number_combinations(numbers, target):
    combinations = set() 

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    # store combination as a sorted tuple to avoid duplicates
                    combinations.add(tuple(sorted((numbers[i], numbers[j], numbers[k]))))

    return combinations

numbers = [1, 2, 3, 4, 5, 6]
target = 10

result = three_number_combinations(numbers, target)
print("Unique combinations of 3 numbers adding to", target, "are:", result)
