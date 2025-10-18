class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        prev = float('-inf')

        for num in nums:
            target = max(num - k , prev + 1)

            if target <= num + k:
                count += 1
                prev = target

        return count