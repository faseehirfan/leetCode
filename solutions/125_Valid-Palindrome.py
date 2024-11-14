# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]

# Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# Solution 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=s.lower()
        s2=[]
        for i in str1:
            if(i.isalnum()):
                s2.append(i)
        s1=s2[::-1]
        return s1==s2