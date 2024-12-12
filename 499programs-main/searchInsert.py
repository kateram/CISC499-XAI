from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)

    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low
nums = [1, 3, 5, 6]
target = 5
solution = Solution()
result = solution.searchInsert(nums, target)
print(f"Target {target} should be inserted at index: {result}")
