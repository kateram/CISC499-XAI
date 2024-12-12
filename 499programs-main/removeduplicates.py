def removeDuplicates(nums):
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow+1] = nums[fast]
            fast += 1
            slow += 1

    return slow + 1
nums = [1, 1, 2, 3, 3, 4]
new_length = removeDuplicates(nums)
print("New Length:", new_length)
print("Modified List (unique elements):", nums[:new_length])