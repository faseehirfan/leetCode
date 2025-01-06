class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        res = float('-inf')
        cur = 0

        for r in range(len(nums)):
            cur += nums[r]

            if r >= k - 1:
                res = max(res, cur/k)
                cur -= nums[l]
                l += 1
        return res

