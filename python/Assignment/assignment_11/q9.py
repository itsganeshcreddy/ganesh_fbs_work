# 9. Write a program to create three lists of numbers, their squares and cubes.

def square_cube_lists(numbers):
    squares = []
    cubes = []
    for num in numbers:
        squares.append(num * num)
        cubes.append(num * num * num)
    return squares, cubes

numbers = [1, 2, 3, 4, 5] 

squares, cubes = square_cube_lists(numbers)

print("Numbers List:", numbers)
print("Squares List:", squares)
print("Cubes List:", cubes)
