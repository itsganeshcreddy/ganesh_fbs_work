# 4. Remove all of the vowels in a string (take input from user) 

s = input('Enter a string:')
res = ''.join([ch for ch in s if(ch not in 'aeiouAEIOU')])
print(res)