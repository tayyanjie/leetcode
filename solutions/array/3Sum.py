"""
Solution of 3 Sum
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/3sum/description/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        countDict = {}
        target = 0
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
        result = set()

        for num in countDict:
            twoSum = target - num

            # Find twoSum
            for num2 in countDict:
                # If num and num2 the same, check that there are multiple of the same
                # num present in original nums list
                if num2 == num and countDict[num] == 1:
                    continue
                remainder = twoSum - num2

                # Check remainder in countDict
                if remainder not in countDict:
                    continue

                if num2 == num:
                    # If remainder same as num ensure that there are at least 3 in countDict
                    if remainder == num:
                        if countDict[num] > 2:
                            result.add((num, num, num))
                    else:
                        result.add(tuple(sorted((num, num, remainder))))
                elif remainder == num2:
                    # If remainder same as num2, check that at least 2 of it in countDict
                    if countDict[num2] >= 2:
                        result.add(tuple(sorted((num, num2, num2))))
                elif remainder == num:
                    # Same as above condition
                    if countDict[num] >= 2:
                        result.add(tuple(sorted((num, num, num2))))
                else:
                    # All nums are different
                    result.add(tuple(sorted((num, num2, remainder))))

        return list(map(list, result))
