import math

def binary_search(lst, target):
    if not lst:
        return -1
    lo = 0
    hi = len(lst)-1

    while lo <= hi:
        mid = math.floor(lo + (hi - lo) / 2)
        if lst[mid] < target:
            lo = mid + 1
        elif lst[mid] > target:
            hi = mid - 1
        elif lst[mid] == target:
            print(f"Found {target} at index {mid}.")
            return mid
    print(f"Target {target} not found.")
    return -1

arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
binary_search(arr, 80)
binary_search(arr, 10)
binary_search(arr, 110)
binary_search(arr, 20)
binary_search(arr, 140)
binary_search(arr, 2)
binary_search(arr, 1)