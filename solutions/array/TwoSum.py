"""
Solution of Two Sum
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]
        for i in range(len(nums)):
            num = nums[i]
            if target - num == num:
                if len(d[num]) >= 2:
                    return d[num][:2]
            elif target - num in d:
                return [i, d[target - num][0]]
