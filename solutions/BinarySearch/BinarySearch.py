"""
Solution of Binary Search
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/binary-search/description/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums sorted in ascending, so if target < first or > last,
        # not found
        if target < nums[0] or target > nums[-1]:
            return -1
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1

        start, end = 0, len(nums) - 1
        # Get mid index and look at either left or right subarray
        # depending on whether target > or < value at mid
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
