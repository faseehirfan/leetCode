## DP solution

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:       
        dp = [[float('inf')] * n for _ in range(k+1)]

        dp[0][src] = 0

        for u,v,price in flights:
            if u == src:
                dp[0][v] = min(dp[0][v], price)

        # fill table for rest

        for i in range(1, k+1):
            for u,v,price in flights:
                dp[i][v] = min(dp[i-1][v], min(dp[i][v], dp[i-1][u] + price))


        return dp[k][dst] if dp[k][dst] < float('inf') else -1
