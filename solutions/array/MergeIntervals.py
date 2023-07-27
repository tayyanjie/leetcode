"""
Solution of Search in Merge Intervals
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/merge-intervals/description/
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # Sort intervals and look through the intervals to find contiguous blocks
        intervals.sort()

        def combine(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        def isOverlap(interval1, interval2):
            if interval1[0] > interval2[0]:
                interval1, interval2 = interval2, interval1
            return interval1[1] >= interval2[0]

        res = []
        # If overlap, combine the intervals setting the 2nd interval
        # as combined interval. Drop first
        # Else, just append the first interval to res
        while len(intervals) > 1:
            if isOverlap(intervals[0], intervals[1]):
                intervals[1] = combine(intervals[0], intervals[1])
                intervals.pop(0)
            else:
                res.append(intervals.pop(0))
        res.extend(intervals)
        return res
