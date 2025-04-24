class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = nums[0], 0

        for n in nums:
            if curSum < 0: curSum = 0
            curSum += n
            res = max(res, curSum)
        return res
    

## dp solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubRecursive(l, r):
            if l == r:
                return nums[l]
            
            mid = l + (r-l) // 2
            left_sum = maxSubRecursive(0, mid)
            right_sum = maxSubRecursive(mid+1,r)
            cross_sum = 0

            count = 0
            max_left = float('-inf')

            for i in range(mid, l - 1, -1):
                count += nums[i]
                max_left = max(count, max_left)
            
            count = 0
            max_right = float('-inf')

            for i in range(mid + 1, r + 1):
                count += nums[i]
                max_right = max(count, max_right)
            
            cross_sum = max_left + max_right

            return max(left_sum, right_sum, cross_sum)


        return maxSubRecursive(0, len(nums)-1)