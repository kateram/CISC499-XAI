from typing import List

class Solution:
    def __init__(self):
        self.start_index = -1
        self.end_index = -1

    def binarySearchFirst(self, arr, low, high, target):
        if low > high:
            return
        mid = (low + high) // 2
        if arr[mid] > target:
            self.binarySearchFirst(arr, low, mid - 1, target)
        elif arr[mid] < target:
            self.binarySearchFirst(arr, mid + 1, high, target)
        else:
            self.start_index = mid
            self.binarySearchFirst(arr, low, mid - 1, target)

    def binarySearchLast(self, arr, low, high, target):
        if low > high:
            return
        mid = (low + high) // 2
        if arr[mid] > target:
            self.binarySearchLast(arr, low, mid - 1, target)
        elif arr[mid] < target:
            self.binarySearchLast(arr, mid + 1, high, target)
        else:
            self.end_index = mid
            self.binarySearchLast(arr, mid + 1, high, target)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.binarySearchLast(nums, 0, len(nums) - 1, target)
        self.binarySearchFirst(nums, 0, len(nums) - 1, target)
        return [self.start_index, self.end_index]


if __name__ == "__main__":
    nums = list(map(int, input("Enter the sorted array (space-separated): ").split()))
    target = int(input("Enter the target value: "))

    solution = Solution()
    result = solution.searchRange(nums, target)

    print(f"Start and End Indices of {target}: {result}")
