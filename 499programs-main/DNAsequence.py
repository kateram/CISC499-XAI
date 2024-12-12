dna = input("Enter a DNA sequence: ")
sequences = dna.split('X')
sequences.sort(key=len, reverse=True)
new_seq = []
for w in sequences:
    if len(w) > 0:
        new_seq.append(w)

print("\nSorted sequences (including empty segments):")
print(sequences)

print("\nNon-empty sorted sequences:")
print(new_seq)
