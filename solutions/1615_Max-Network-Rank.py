class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)

        for c1, c2 in roads:
            graph[c1].add(c2)
            graph[c2].add(c1)

        res = 0

        for c1, c2 in combinations(graph.keys(), 2):
            is_connected = 1 if c1 in graph[c2] else 0
            rank = len(graph[c1]) + len(graph[c2]) - is_connected
            res = max(res, rank)

        return res