#  You are given an integer array nums of size n.

# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

# In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.

# The bitwise AND of an array is the bitwise AND of all the numbers in it.

# A subarray is a contiguous sequence of elements within an array. 

# SOLUTION:

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = maxLen = curLen = 0

        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxLen = 1
                curLen = 1
            elif nums[i] < maxVal:
                curLen = 0
            elif nums[i] == maxVal:
                curLen += 1

            maxLen = max(curLen, maxLen)

        return maxLen

