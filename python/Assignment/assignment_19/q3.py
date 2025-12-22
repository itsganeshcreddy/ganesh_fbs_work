# 3. Count the number of spaces in a string (take input from user)

s = input('Enter a string:')
count = len([ch for ch in s if(ch == ' ')])
print('Spaces:', count)