# 2 Pointer O(n) TC and O(1) SC
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = rightSum = 0
        for n in nums:
            rightSum += n
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum: return i
            leftSum += nums[i]
        return -1

# Prefix Sum O(n) TC and O(n) SC
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        for i in range(len(nums)):
            if prefix[i] - nums[i] == prefix[-1] - prefix[i]:
                return i
        return -1
