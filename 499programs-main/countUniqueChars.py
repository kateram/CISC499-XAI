s = input("Enter a string: ")
unique = ''
for c in s:
    if c not in unique:
        unique += c
print("Number of unique characters:", len(unique))