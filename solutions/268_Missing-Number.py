# Bit Manipulation, O(n) time, O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = xor_nums = 0

        for i in range(n + 1):
            xor_all ^= i

        for num in nums:
            xor_nums ^= num

        return xor_all ^ xor_nums
        

# Gauss' Formula, O(n) time, O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = n*(n+1) // 2
        return target - sum(nums)

# Hash Set, O(n) time, O(n) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set([i for i in range(len(nums)+1)])

        for n in nums:
            numset.remove(n)

        return list(numset)[0]