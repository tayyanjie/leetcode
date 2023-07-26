"""
Solution of Rotting Oranges
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        last_num = nums[-1]
        left, right = 0, len(nums) - 1

        # Find Pivot Index, pivot is leftmost
        # element <= nums[-1]
        pivot_ind = -1
        mid = (left + right) // 2
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            # left most <= nums[-1] found
            if nums[left] <= last_num:
                pivot_ind = left
                break

            mid = (left + right) // 2
            # since nums[mid] <= last num
            # check the left subarray including
            # mid index to find left most num <= nums[-1]
            if nums[mid] <= last_num:
                right = mid
            # Else, look at right subarray, excluding mid
            else:
                left = mid + 1
        if pivot_ind == -1:
            pivot_ind = mid

        # Based on pivot index, determine whether
        # to search from left subarray or right subarray
        # split by pivot index
        if target < nums[0] and pivot_ind > 0:
            left, right = pivot_ind, len(nums) - 1
        elif target > nums[0] and pivot_ind > 0:
            left, right = 0, pivot_ind - 1
        elif pivot_ind <= 0:
            left, right = 0, len(nums) - 1
        else:
            return -1

        # Perform binary search on the subarray
        while left < right:
            if target < nums[left] or target > nums[right]:
                return -1
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
