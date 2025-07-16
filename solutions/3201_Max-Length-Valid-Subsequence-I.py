class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                parity = (nums[j] + nums[i]) % 2
                dp[i][parity] = max(dp[i][parity], dp[j][parity] + 1)
                max_len = max(max_len, dp[i][parity])
        
        return max_len