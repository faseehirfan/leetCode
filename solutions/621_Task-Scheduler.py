class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        hp = [-v for v in count.values()]
        heapq.heapify(hp)
        q = deque()
        time = 0

        while hp or q:
            time += 1
            if hp:
                cnt = 1 + heapq.heappop(hp)
                if cnt:
                    q.append((cnt, n + time))
            if q and q[0][1] == time:
                heapq.heappush(hp, q.popleft()[0])

        return time