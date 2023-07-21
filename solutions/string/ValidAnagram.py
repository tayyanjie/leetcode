"""
Solution of Valid Anagram
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/valid-anagram/description/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countDict = {}
        for char in s:
            if char in countDict:
                countDict[char] += 1
            else:
                countDict[char] = 1
        for char in t:
            if char not in countDict:
                return False
            else:
                if countDict[char] == 1:
                    del countDict[char]
                else:
                    countDict[char] -= 1
        return True
