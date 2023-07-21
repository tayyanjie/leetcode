"""
Solution of Maximum Subarray
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/maximum-subarray/description/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Less space efficient solution
        # Reference: https://tutorialhorizon.com/algorithms/dynamic-programming-maximum-subarray-problem/
        # dp[i] is the maximum sum of a contiguous array ending at index i
        # dp = [nums[0]]
        # for i in range(1, len(nums)):
        #     # max sum at index i is either add num at index i or start new array
        #     # by itself using num at index i
        #     dp.append(max(dp[i-1] + nums[i], nums[i]))
        # return max(dp)

        dp = nums[0]
        max_value = dp
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            max_value = max(dp, max_value)
        return max_value
