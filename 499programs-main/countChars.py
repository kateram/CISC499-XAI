print("Enter a block of text (press Enter twice to finish):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = "\n".join(lines)
count = {}
for char in text:
    if char == '\n':
        continue
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1
print("\nCharacter Frequencies:")
for key in sorted(count.keys()):
    print("'{}' {}".format(key, count[key]))
