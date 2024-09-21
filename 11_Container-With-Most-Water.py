# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1 
        max_val = 0
        while (l <= r):
            h = height[l] if height[l] < height[r] else height[r]
            area = h * (r-l)
            max_val = max(area, max_val)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_val
        