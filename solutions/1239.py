class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(s):
            count = Counter(charSet) + Counter(s)
            return max(count.values()) > 1

        def backtrack(i):
            if i == len(arr): return len(charSet)
            res = 0

            if not overlap(arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    charSet.remove(c)

            return max(backtrack(i+1), res)
        
        return backtrack(0)
