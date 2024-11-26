class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, combo, cur_sum):
            if cur_sum == target:
                res.append(combo.copy())
                return
            if i >= len(candidates) or cur_sum > target:
                return 

            combo.append(candidates[i])
            backtrack(i, combo, cur_sum + candidates[i])
            combo.pop()
            backtrack(i+1, combo, cur_sum)

        backtrack(0, [], 0)
        return res
