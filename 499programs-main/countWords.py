celestial_objects = input("Enter celestial objects separated by commas: ").split(',')
celestial_objects = [obj.strip() for obj in celestial_objects]
names = []
counter = []
for name in celestial_objects:
    if name in names:
        idx = names.index(name)
        counter[idx] += 1
    else:
        names.append(name)
        counter.append(1)
print("\nCounts of celestial objects:")
for i in range(len(names)):
    print("{:12} {}".format(names[i], counter[i]))
