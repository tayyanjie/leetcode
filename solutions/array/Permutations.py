"""
Solution of Permutations
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/permutations/description/
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Store perm with length 0 to expand
        d = {0: [[]]}
        # Iteratively build up permutation from
        # permutation of 1 less length from previous iteration
        for i in range(1, len(nums) + 1):
            # Get permutation from previous iteration and build
            # permutation of length i from there
            perms = d[i - 1]
            new_perms = []
            for perm in perms:
                # flag to indicate if the original perm
                # has a value appended (this is done to save storage)
                flag = False
                for num in nums:
                    if num not in perm:
                        # If first time adding a new perm
                        # built from perm, then append to perm the num
                        # else create copy and modify element at last index
                        if flag:
                            new_perm = perm.copy()
                            new_perm[-1] = num
                            new_perms.append(new_perm)
                        else:
                            perm.append(num)
                            new_perms.append(perm)
                        flag = True
            # add all perms to dictionary
            d[i] = new_perms
        # return all permutations with length len(nums)
        return d[len(nums)]
