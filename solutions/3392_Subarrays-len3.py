class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 2
        res = 0
        while r < len(nums):
            if nums[l] + nums[r] == nums[r-1] / 2:
                res += 1
            r += 1
            l += 1
        return res