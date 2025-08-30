class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        cur_sum = 0
        res = float('inf')

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return 0 if res == float('inf') else res
