"""
Solution of Combination Sum
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/combination-sum/description/
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Returns list of unique combinations of candidates where the sum = target
        A candidate may be picked multiple times and all candidates >= 2
        """

        # {number of candidates:[([candidate1, ..., candidateK], sum of candidates), (..., ...)]}
        combinations = {0: [([], 0)]}

        # Sort the candidates
        candidates = sorted(candidates)

        # Result containing all combinations
        res = set()

        for i in range(1, target):
            # Build possible combinations from possibilities
            # that have 1 less candidate in combination
            c = combinations[i - 1]

            # Store all the tuples of (combination, sum)
            # for combinations that have length i
            c2 = []

            # iterate through all combination that have i-1 elements
            for comb, total in c:
                residual = target - total

                for candidate in candidates:
                    # candidates sorted so if candidate > residual,
                    # all later candidates need not be looked at
                    if candidate > residual:
                        break
                    # only add candidates in ascending order, so all
                    # combination stored will be in ascending order
                    # so if candidate less than the latest value, skip that
                    if len(comb) > 0 and candidate < comb[-1]:
                        continue
                    # create new copy of the combination
                    # as lists are mutable
                    new_comb = comb.copy()
                    new_comb.append(candidate)

                    # If total + candidate = target, just add to result
                    # do not have to add to the list of combinations
                    # as no addition of any new numbers will allow it to achieve
                    # target since all numbers in candidates >= 2
                    if total + candidate == target:
                        res.add(tuple(new_comb))
                    # If greater target, can ignore as well
                    elif total + candidate < target:
                        c2.append((new_comb, total + candidate))
            # If no possible combinations, then can end loop as the next loop
            # depends on c2
            if len(c2) == 0:
                break
            combinations[i] = c2

        return [list(vals) for vals in res]
