# Solution 1 Sliding window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = cur = 0
        l = r = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1

        return res

# Solution 2 DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]
        r = 1

        while r < len(prices):
            if prices[r] < minBuy:
                minBuy = prices[r]
            else: 
                res = max(prices[r] - minBuy, res)
            r += 1
        return res
