class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1: return s
        count = Counter(s)
        maxHeap = [(-v,k) for k,v in count.items()]
        heapq.heapify(maxHeap)
        if -(maxHeap[0][0]) > (len(s) + 1) // 2: return ""

        prev = None
        res = []

        while maxHeap or prev:
            cnt, char = heapq.heappop(maxHeap)
            res.append(char)
            cnt += 1

            if prev: 
                heapq.heappush(maxHeap, prev)
                prev = None 
            if cnt:
                prev = (cnt, char)

        return ''.join(res)