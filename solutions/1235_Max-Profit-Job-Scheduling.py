
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)

        p = [-1] * n

        for i in range(n):
            l, r = 0, i-1

            while l <= r:
                mid = (r+l) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    p[i] = mid
                    l = mid + 1
                else:
                    r = mid - 1 

        dp = [0] * n
        for i in range(n):
            prev_profit = dp[i-1] if i > 0 else 0
            potential_profit = jobs[i][2]
            if p[i] != -1:
                potential_profit += dp[p[i]]
            
            dp[i] = max(potential_profit, prev_profit)


        return dp[-1]
            
# OR

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n= len(startTime)

        ends = [job[1] for job in jobs]
        dp = [0] * n 
        dp[0] = jobs[0][2]
        for i in range(1, n):
            s, e, p = jobs[i]
            not_take = dp[i - 1]
            j = bisect.bisect_right(ends, s) - 1 
            take = p
            if j >= 0:
                take += dp[j]
            dp[i] = max(not_take, take)
        return dp[-1]

# binary search: for i, find j < i whose endtime <= starttime[i]
# dp[i]=max profit for jobs upto i
# 1: skip job 1 dp[i]=dp[i-1]
# 2: i, dp[i]=profit[i] + dp[j]
#  return dp[n-1]


# OR
