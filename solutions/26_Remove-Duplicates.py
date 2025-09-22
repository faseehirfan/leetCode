class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0

        for r in range(1, n):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

        return l + 1
