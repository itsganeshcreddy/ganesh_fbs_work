# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def generate_squares(n):

    squares_dict = {x: x*x for x in range(1, n+1)}
    return squares_dict

n = int(input("Enter a number: "))
result = generate_squares(n)

print("Dictionary of numbers and their squares:", result)
