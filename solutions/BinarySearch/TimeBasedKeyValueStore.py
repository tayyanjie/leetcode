"""
Time Based Key-Value Store
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/time-based-key-value-store/description/
"""


class TimeMap:
    def __init__(self):
        self.storage = {}  # stores exact timestamp and corresponding value
        self.storage_timestamps = {}  # stores list of timestamps in ascending order

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = {timestamp: value}
            self.storage_timestamps[key] = [timestamp]
        else:
            self.storage[key][timestamp] = value
            self.storage_timestamps[key].append(timestamp)

    def binarySearch(self, timestamps, target):
        """
        Perform binary search to find index of timestamp to use which
        is the largest timestamp <= target. If not found, return -1
        """
        if target < timestamps[0]:
            return -1
        left, right = 0, len(timestamps) - 1
        while left < right - 1:
            if timestamps[left] == target:
                return left
            if timestamps[right] == target:
                return right
            mid = (left + right) // 2
            if target == timestamps[mid]:
                return mid
            if target < timestamps[mid]:
                right = mid - 1
            else:
                left = mid
        if target >= timestamps[left] and target >= timestamps[right]:
            return right
        return (left + right) // 2

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        if timestamp in self.storage[key]:
            return self.storage[key][timestamp]
        timestamps = self.storage_timestamps[key]
        ts_ind = self.binarySearch(timestamps, timestamp)
        ts = timestamps[ts_ind]
        return self.storage[key][ts] if ts_ind != -1 else ""
