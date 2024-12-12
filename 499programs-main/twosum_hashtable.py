def twoSum(nums, target):
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                print([i, numMap[complement]])

        return []

twoSum([2, 7, 11, 15], 9)