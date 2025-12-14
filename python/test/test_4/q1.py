# 1.Write a function to which we pass a parameter and print the factors of a given number.
# eg: Factors of 12 : 1,2,3,4,6,12

def factors(num):
    print(f"Factors of {num} are:")
    for i in range(1, num + 1):
        if(num % i == 0):        # if i divides num completely
            print(i, end=" ")

n = int(input("Enter a number: "))
factors(n)

