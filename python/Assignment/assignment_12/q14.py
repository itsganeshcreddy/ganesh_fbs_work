# 14. Python Program to count the occurrences of each word in a string.


text = 'python is easy python is fun'

words = text.split()

# dictionary
word_count = {}

# Count each word
for word in words:
    if(word in word_count):
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word in word_count:
    print(word, ":", word_count[word])
