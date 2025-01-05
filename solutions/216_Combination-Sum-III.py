class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(i, combo, cur_sum):
            if cur_sum == n and len(combo) == k:
                res.append(combo.copy())
                return
            if i >= 10 or cur_sum >= n: return

            combo.append(i)
            backtrack(i+1, combo, cur_sum + i) 
            combo.pop()
            backtrack(i+1, combo, cur_sum)

        backtrack(1, [], 0)
        return res
        