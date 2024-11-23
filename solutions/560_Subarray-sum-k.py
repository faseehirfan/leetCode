class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_dict = {0 : 1}
        sum = 0
        for n in nums:
            sum += n
            if sum - k in pre_dict:
                res += pre_dict[sum-k]
            pre_dict[sum] = 1 + pre_dict.get(sum, 0)
            

        return res