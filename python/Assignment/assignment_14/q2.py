# 2. Write a Python program to remove the intersection of a second set with a first set.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.difference_update(set2)
print("Set after removing intersection:", set1)
