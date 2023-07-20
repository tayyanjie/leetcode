"""
Solution of Product of Array Except Self
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/product-of-array-except-self/description/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = len(nums) * [1]
        for i in range(len(nums) - 1):
            # Product at index i is the product of all nums at index < i
            ans[i + 1] = ans[i] * nums[i]

        # Example: nums = [2,2,4,1]
        # At this stage, ans = [1,2,4,12], final result to get i.e., res = [24,24,16,12]
        # res[2] = nums[2] * ans[2]
        # res[1] = nums[1] * nums[2] * ans[1]
        # Postfix needed to store the nums[2]*nums[1]*nums[0]

        # Create postfix to hold the latest value to multiply from the back
        postfix = 1

        # Multiply the elements from the back
        for j in range(len(nums) - 2, -1, -1):
            postfix *= nums[j + 1]
            ans[j] *= postfix
        return ans
