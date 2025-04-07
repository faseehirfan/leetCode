class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for n in nums:
            if steps < 0:
                return False
            elif n > steps:
                steps = n
            steps -= 1
            
        return True