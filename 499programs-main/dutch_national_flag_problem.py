def dutch_national_flag_problem(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter an array of 0s, 1s, and 2s (space-separated): ").split()))

    if not all(x in [0, 1, 2] for x in arr):
        print("Error: Please enter an array containing only 0s, 1s, and 2s.")
    else:
        result = dutch_national_flag_problem(arr)
        print("Sorted Array:", result)
