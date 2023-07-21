"""
Solution of Valid Parentheses
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["{", "(", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
