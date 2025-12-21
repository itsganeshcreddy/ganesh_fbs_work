# 6.Use a dictionary comprehension to count the length of each word in a sentence (take input from user) 

s = input('Enter a string:')
words = s.split()

res = {w : len(w) for w in words}
print(res) 