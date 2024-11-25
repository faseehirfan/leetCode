class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = nums[0], 0

        for n in nums:
            if curSum < 0: curSum = 0
            curSum += n
            res = max(res, curSum)
        return res