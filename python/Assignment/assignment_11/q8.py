# 8. Print 1 to 100 in snakes and ladder pattern.

def snake_ladder_pattern(n, cols):
    for i in range(0, n, cols):
        row = list(range(i + 1, i + cols + 1))  
        
        # Reverse alternate rows
        if (i // cols) % 2 == 1:
            row.reverse()
        
        for num in row:
            print(f"{num:3}", end=" ")
        print()  

n = 100
cols = 10
snake_ladder_pattern(n, cols)
