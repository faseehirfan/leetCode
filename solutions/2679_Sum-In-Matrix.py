class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n, m = len(nums), len(nums[0])
        res = 0

        for i in range(n):
            nums[i].sort(reverse=True)

        for j in range(m):
            cur_max = -1
            for i in range(n):
                cur_max = max(cur_max, nums[i][j])
            
            res += cur_max

        return res



    # def matrixSum(self, nums: List[List[int]]) -> int:
    #     res = 0
    #     removed = 0
    #     size = len(nums) * len(nums[0])

    #     while removed < size:
    #         row_max = -1

    #         for i in range(len(nums)):
    #             cur_max = -1
    #             max_index = -1
    #             for j in range(len(nums[0])): 
    #                 num = nums[i][j]
    #                 if num > cur_max:
    #                     cur_max = num
    #                     max_index = j

    #             nums[i][max_index] = -1
    #             removed += 1
    #             row_max = max(cur_max, row_max)

    #         res += row_max

    #     return res
        

            