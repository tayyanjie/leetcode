"""
Solution of Longest Substring Without Repeating Characters
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxLength = 0

        # left and right pointers for substring
        left, right = 0, 0

        # Store all letters in current substring
        d = set()

        while left <= right < len(s):
            # If next char not in current substring, add it
            # to the dict of chars
            s_right = s[right]
            if s_right not in d:
                d.add(s_right)
            # else get update maxLength and
            # move left pointer until s[right] is not in d
            else:
                maxLength = max(maxLength, len(d))
                while left < right:
                    if s[left] == s_right:
                        left += 1
                        break
                    else:
                        d.remove(s[left])
                        left += 1
            right += 1

        maxLength = max(maxLength, len(d))

        return maxLength
