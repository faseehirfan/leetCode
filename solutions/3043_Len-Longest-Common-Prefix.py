class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        res = 0
        
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10


        for num in arr2:
            while num > 0:
                if num in prefixes:
                    res = max(res, len(str(num)))
                num //= 10

        return res