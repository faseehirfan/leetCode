class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()

        for num in arr:
            cur = {num}
            for p in prev:
                cur.add(p | num)
            
            prev = cur
            res.update(cur)

        return len(res)
