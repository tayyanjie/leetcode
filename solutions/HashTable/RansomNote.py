"""
Solution of Ransom Note
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/ransom-note/description/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Returns whether ransomNote can be constructed from letters in magazine
        """
        # If more chars in ransomNote, then ransomNote cannot be constructed
        if len(magazine) < len(ransomNote):
            return False

        # Create a dictionary to store char count of ransomNote
        d = {}
        for char in ransomNote:
            d[char] = d[char] + 1 if char in d else 1

        # Loop through chars in magazine
        # Remove chars from dict until its empty
        # Once empty, means that ransomNote can be constructed
        for char in magazine:
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    del d[char]
            if len(d) == 0:
                return True

        return False
