class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        stack = []
        def backtrack(index):
            if index >= len(nums):
                res.append(stack[:])
                return

            stack.append(nums[index])
            backtrack(index+1)
            stack.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index+1)

        backtrack(0)

        return res