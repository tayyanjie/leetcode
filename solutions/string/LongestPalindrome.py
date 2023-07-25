"""
Solution of Longest Palindrome
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/longest-palindrome/description/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        The length of longest palindrome that ca be built from s is
        the sum of number of letters (for letters with even count) and the number of letters - 1
        (for each unique letter with odd count). If there is any odd count, add 1 to the final result
        as that letter can be the centre of the palindrome.
        """
        res = 0

        # When encounter the odd number of time, add
        # to set. If encounter even number'th time, remove from set
        d = set()
        for char in s:
            if char not in d:
                d.add(char)
            else:
                d.remove(char)
                # Add 2 to count
                res += 2
        if d:
            # If any odd count add 1 to final result
            res += 1
        return res
