class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, combo, total):
            if total == target: 
                res.append(combo.copy())
                return
            if total > target or i >= len(candidates): return 

            #include candidates[i]
            combo.append(candidates[i])
            backtrack(i+1, combo, total + candidates[i])
            combo.pop()

            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, combo, total)

        backtrack(0, [], 0)
        return res
