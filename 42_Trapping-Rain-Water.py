# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax <= rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res