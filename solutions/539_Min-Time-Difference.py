class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = 24 * 60

        def time_to_minutes(time):
            hours, minutes = time.split(':')
            return (int(hours) * 60) + int(minutes)

        def get_time_difference(time1, time2):
            return time1 - time2

        minutes = sorted(time_to_minutes(t) for t in timePoints)

        for i in range(1, len(minutes)):
            prev_time = minutes[i - 1]
            cur_time = minutes[i]
            res = min(res, get_time_difference(cur_time, prev_time))

        res = min(res, 24*60 - get_time_difference(minutes[-1], minutes[0]))
        return res
