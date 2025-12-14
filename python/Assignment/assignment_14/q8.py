# 8. Write a Python program to find all the anagrams and group them together from a given list of strings.

def group_anagrams(words):
    grouped = []
    seen = set()

    for word in words:
        if(word in seen):
            continue

        # find all words that are anagrams of current word
        group = [w for w in words if sorted(w) == sorted(word)]
        
        grouped.append(group)

        # mark all words in this group as seen
        for w in group:
            seen.add(w)

    return grouped

words = ["cat", "dog", "tac", "god", "act"]

result = group_anagrams(words)
print("Grouped Anagrams:", result)
