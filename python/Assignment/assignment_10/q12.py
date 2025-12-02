# 12 . Write a program to create three lists of numbers, their squares and cubes.

def create_lists(li):
    squares = []
    cubes = []
    
    for x in li:
        squares.append(x * x)
        cubes.append(x * x * x)
    
    return squares, cubes

n = int(input("How many elements? "))
li = []

for i in range(n):
    li.append(int(input(f"Enter element {i+1}: ")))

squares, cubes = create_lists(li)

print("Numbers List:", li)
print("Squares List:", squares)
print("Cubes List:", cubes)
