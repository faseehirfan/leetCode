class Solution:
    def rob(self, nums: List[int]) -> int:

        
        def helper(l,r):
            rob1 = rob2 = 0
            
            for i in range(l,r):
                newRob = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], helper(1,len(nums)), helper(0, len(nums)-1))
