#  5. Find all of the words in a string that are less than 5 letters (take input from user) 

s = input('Enter string:')
words = s.split()

res = [w for w in words if(len(w) < 5)]
print(res)