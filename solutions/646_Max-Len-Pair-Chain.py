class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        res = 1
        prev = pairs[0]

        for i in range(1, len(pairs)):
            if prev[1] < pairs[i][0]:
                res += 1
                prev = pairs[i]

        return res
    
    # DP solution is similar to LIS. These quesitions are vitually the same. 