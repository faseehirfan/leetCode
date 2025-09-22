class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        matched = nums[0]

        for num in nums:
            if num == matched:
                count -= 1
            else:
                count += 1
                if count >= 0:
                    matched = num
                    count = -1

        return matched
