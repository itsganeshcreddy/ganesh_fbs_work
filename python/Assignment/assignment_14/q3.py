# 3. Write a Python program to find all the unique words and count the frequency of occurrence
#    from a given list of strings. Use Python set data type.

sentences = ["apple banana apple", "banana orange apple"]

unique_words = set()  
for sentence in sentences:
    words = sentence.split()  # split each sentence into words
    unique_words.update(words)  # add words to the set

print("Unique words:", unique_words)

# Count frequency of each word
word_count = {}  
for sentence in sentences:
    for word in sentence.split():
        word_count[word] = word_count.get(word, 0) + 1  # count occurrence

print("Word frequencies:", word_count)
