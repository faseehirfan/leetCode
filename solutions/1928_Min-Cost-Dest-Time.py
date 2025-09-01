class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        n = len(passingFees)

        g = defaultdict(list)

        for edge1, edge2, time in edges:
            g[edge1].append((edge2, time))
            g[edge2].append((edge1, time))

        times = {}

        pq = [(passingFees[0], 0, 0)]

        while pq:
            cost, time, node = heapq.heappop(pq)

            if time > maxTime:
                continue

            if node == n - 1:
                return cost

            if node not in times or times[node] > time:
                times[node] = time
                for nbor, trip in g[node]:
                    heapq.heappush(pq, (passingFees[nbor] + cost, time + trip, nbor))

        return -1


# super hard q intuitively but solution is very clean and makes sense