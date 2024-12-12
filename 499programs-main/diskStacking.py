def DiskStacking(disks):
    disks.sort(key=lambda x: x[2])
    heights = [disk[2] for disk in disks]
    sequences = [-1 for _ in disks]
    for i in range(1, len(disks)):
        current_disk = disks[i]
        for j in range(i):
            other_disk = disks[j]
            if are_valid_dimensions(other_disk, current_disk):
                if heights[i] <= current_disk[2] + heights[j]:
                    heights[i] = current_disk[2] + heights[j]
                    sequences[i] = j
    max_index = heights.index(max(heights))
    sequence = build_sequence(disks, sequences, max_index)
    return sequence

def are_valid_dimensions(other_disk, current_disk):
    return other_disk[0] < current_disk[0] and other_disk[1] < current_disk[1] and other_disk[2] < current_disk[2]

def build_sequence(disks, sequences, index):
    sequence = []
    while index != -1:
        sequence.append(disks[index])
        index = sequences[index]
    sequence.reverse()
    return sequence

if __name__ == "__main__":
    print("Enter the dimensions of disks as a list of [width, depth, height]:")
    disks = eval(input("For example, [[2, 1, 2], [3, 2, 3], [2, 2, 8]]: "))
    result = DiskStacking(disks)
    print("\nThe sequence of disks for the maximum height stack is:")
    print(result)
