"""
Solution of First Bad Version
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/first-bad-version/description/
"""


# Dummy isBadVersion, the leetcode isBadVersion has been pre-defined
# This function is just a dummy placeholder.
def isBadVersion(version: int) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Base case, if n == 1, 1 must be the bad
        # version since bad >= 1
        if n == 1:
            return 1

        # Perform Binary Search for the first bad version
        mid = n // 2
        left, right = 1, n
        while left > 0 and right <= n:
            # If mid is bad version, first bad version must be right
            # of or equal to mid
            if isBadVersion(mid):
                right = mid
            # If not bad version, that means first bad version
            # mus be right of mid
            else:
                left = mid + 1
            new_mid = (left + right) // 2

            # If mid == new_mid, means no other values to check
            # within window so that must be first bad version
            if mid == new_mid:
                return mid
            mid = new_mid
        return mid
