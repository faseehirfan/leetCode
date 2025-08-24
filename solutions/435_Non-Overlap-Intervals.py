class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prev_end_time = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prev_end_time <= intervals[i][0]:
                prev_end_time = intervals[i][1]
            else:
                res += 1

        return res
