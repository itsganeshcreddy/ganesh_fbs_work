# 3.WAP to print following pattern.

n = int(input("Enter size of Z: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:     # first or last row
            print("*", end=" ")
        elif j == n - i - 1:       # diagonal
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


