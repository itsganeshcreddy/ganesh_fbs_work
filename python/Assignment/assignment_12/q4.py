# 4. Python Program to Form a New String where the First Character and 
#     the Last Character have been Exchanged 

text = input("Enter a string: ")

# Swap first and last characters
if(len(text) > 1):
    new_text = text[-1] + text[1:-1] + text[0]
else:
    new_text = text 

print("Modified string:", new_text)
