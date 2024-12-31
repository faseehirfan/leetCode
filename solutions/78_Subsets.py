class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(index):
            if index >= len(nums):
                res.append(stack[:])
                return
            stack.append(nums[index])
            backtrack(index+1)
            stack.pop()
            backtrack(index+1)

        backtrack(0)

        return res