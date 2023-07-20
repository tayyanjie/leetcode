"""
Solution of Insert Interval
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/insert-interval/description/
"""

from typing import List


class Solution:
    @staticmethod
    def is_overlap(interval1, interval2):
        """
        Checks whether there is overlap between interval1 and interval2
        """
        if interval1[0] > interval2[0]:
            interval1, interval2 = interval2, interval1
        elif interval1[0] == interval2[0] and interval1[1] < interval2[1]:
            interval1, interval2 = interval2, interval1
        return interval1[1] >= interval2[0]

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # No interval, return newInterval
        if not intervals:
            return [newInterval]
        # New interval to be inserted in first location, no overlap
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        # New interval inserted in last location, no overlap
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        # Find index of start and end overlap
        start_overlap_index = -1
        end_overlap_index = -1
        for i in range(len(intervals)):
            if i < len(intervals) - 1:
                # If find position with no overlap, then insert it there and return
                if (
                    newInterval[0] > intervals[i][1]
                    and newInterval[1] < intervals[i + 1][0]
                ):
                    intervals.insert(i + 1, newInterval)
                    return intervals
            if self.is_overlap(intervals[i], newInterval):
                if start_overlap_index == -1:
                    start_overlap_index = i
                # regardless end overlap index is the latest overlap index
                end_overlap_index = i
            # If no more overlap and overlap has been found, break loop as the correct
            # end overlap index has been found
            elif end_overlap_index != -1:
                break

        # If no end overlap is found and start overlap is found then
        # remove all intervals after start overlap interval and update start overlap interval
        if start_overlap_index != -1 and end_overlap_index == -1:
            start_interval = intervals[start_overlap_index]
            end_interval = intervals[-1]
            intervals[start_overlap_index] = [
                min(start_interval[0], newInterval[0]),
                max(end_interval[1], newInterval[1]),
            ]
            return intervals[: start_overlap_index + 1]

        # Combine the overlaps
        res = []
        i = 0
        l = len(intervals)
        while i < l:
            if i < start_overlap_index:
                res.append(intervals.pop(0))
                i += 1
            elif i > end_overlap_index:
                res.append(intervals[i - start_overlap_index])
                i += 1
            elif i == start_overlap_index:
                start_interval = intervals[0]
                end_interval = intervals[end_overlap_index - start_overlap_index]
                ins_interval = [
                    min(newInterval[0], start_interval[0]),
                    max(newInterval[1], end_interval[1]),
                ]
                res.append(ins_interval)
                i = end_overlap_index + 1
        return res
