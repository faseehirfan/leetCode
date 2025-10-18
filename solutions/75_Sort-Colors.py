class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3

        for n in nums:
            freq[n] += 1

        color = 0

        for i in range(len(nums)):
            while freq[color] == 0:
                color += 1

            nums[i] = color
            freq[color] -= 1
        
        return nums