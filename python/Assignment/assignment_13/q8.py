# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

text = "apple banana apple orange banana apple"

words = text.split()

fr_dict = {}                  # empty dict to store frequency

# count the frequency of each word
for word in words:
    if(word in fr_dict):
        fr_dict[word] += 1
    else:
        fr_dict[word] = 1

print("Word Frequencies:", fr_dict)
