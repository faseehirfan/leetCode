class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        graph = collections.defaultdict(set)

        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)

        for city1, city2 in itertools.combinations(graph.keys(), 2):
            is_connected = 1 if city1 in graph[city2] else 0
            rank = len(graph[city1]) + len(graph[city2]) - is_connected
            res = max(res, rank)

        return res