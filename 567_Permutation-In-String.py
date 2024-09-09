# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# SOLUTION BELOW

from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        s1count, n, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in s1count: 
                s1count[s2[i]] -= 1 # character from s2 is in s1, so decrement 1 from its frequency map
                if s1count[s2[i]] == 0:
                    matched += 1    # increment number of matched characters when frequency is 0
            
            # case for when i >= len(s1), this now becomes a sliding window problem.
            # when we slide, we need to increment the frequency of the char thats leaving the window. 
            if i >= n and s2[i-n] in s1count: 
                if s1count[s2[i-n]] == 0: # i-n represents the beginning of the window 
                    matched -= 1
                s1count[s2[i-n]] += 1
            
            if matched == len(s1count):
                return True
            
        return False
    
# TAKEAWAYS:

# Making use of the Counter class from the collections module:
# can count the occurrences of each item in an iterable, such as a list or a string.
# makes solving this question a lot easier, without the counter module, you would need to build the frequency map yourself, 
# which isn't hard, can be done in linear time. 