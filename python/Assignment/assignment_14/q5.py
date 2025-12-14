# 5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_prefix(words):
    prefix = ""

    # find the shortest word
    small = min(words, key=len)

    for i in range(len(small)):
        # take characters at position i from all words using set
        s = {word[i] for word in words}

        if(len(s) == 1):                            # all characters are same
            prefix += small[i]
        else:
            break

    return prefix

words = input("Enter words: ").split()

result = longest_prefix(words)
print("Longest Common Prefix:", result)
