"""
Solution of Climbing Stairs
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/climbing-stairs/description/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        # DP Solution:
        # number of steps to reach k = num steps to k-1 + num steps
        # to k-2
        # dp = (n+1)*[0]
        # dp[0], dp[1] = 1, 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[-1]

        # Convert DP solution to more efficient solution
        a, b = 2, 3
        for i in range(3, n):
            a, b = b, a + b

        return b
