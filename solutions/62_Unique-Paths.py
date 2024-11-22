class Solution:
    # Brute Force
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        if m == 0 or n == 0: return 0
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    # DP (Memoization)
    def uniquePaths(self, m: int, n: int) -> int:


        def dp(m, n, memo=None):
            if memo is None: memo = {}
            # Always store with the smaller value first
            key = (min(m, n), max(m, n))
            if key in memo: return memo[key]
            if m == 1 and n == 1: return 1
            if m == 0 or n == 0: return 0
            memo[key] = dp(m-1, n, memo) + dp(m, n-1, memo)
            return memo[key]

        return dp(m, n)

    # DP (Tabulation)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(m+1):
            for j in range(n+1):
                current = dp[i][j]
                if i + 1 <= m: dp[i+1][j] += current
                if j + 1 <= n: dp[i][j+1] += current
        return dp[m][n]