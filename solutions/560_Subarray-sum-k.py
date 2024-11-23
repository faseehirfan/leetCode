class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_dict = {0 : 1}
        sum = 0
        for n in nums:
            sum += n
            res += pre_dict.get(sum - k, 0)
            pre_dict[sum] = 1 + pre_dict.get(sum, 0)
            
        return res
