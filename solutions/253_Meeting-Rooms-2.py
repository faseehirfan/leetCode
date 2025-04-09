"""
Problem: Meeting Rooms II (Interval Coloring)

You are given an array of meeting time intervals consisting of start and end times:
    intervals[i] = [start_i, end_i]

Return the **minimum number of conference rooms** required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6
"""

from typing import List
import heapq

def minMeetingRooms(intervals: List[List[int]]) -> int:
    # Your code here
    intervals.sort(key=lambda x: x[0])
    color_count = 0
    heap = [] # heap of rooms in use. 
    free_colors = [] # heap of availible colors
    for start, end in intervals:
      if heap and heap[0][0] <= start:
        _, color = heapq.heappop(heap)
        heapq.heappush(free_colors, color)

      if free_colors:
        color = heapq.heappop(free_colors)
      else:
        color_count += 1
        color = color_count

      heapq.heappush(heap, (end, color))
    return color_count
    

intervals = [
    [0, 10],
    [5, 15],
    [10, 20],
    [15, 25],
    [20, 30],
    [25, 35]
]
print(minMeetingRooms(intervals))  # Expected output: 2
