"""
Solution of Coin Change
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/coin-change/description/
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization, alternatively use @cache to memoize
        d = {0: 0}
        total = amount

        def helper(amount):
            if amount in d:
                return d[amount]
            if amount < 0:
                return total + 1
            min_change = total + 1
            for coin in coins:
                min_change = min(min_change, helper(amount - coin) + 1)
            d[amount] = min_change
            return min_change

        res = helper(amount)
        if res > amount:
            return -1
        else:
            return res
