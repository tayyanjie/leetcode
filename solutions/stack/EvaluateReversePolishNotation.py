"""
Solution of Evaluate Reverse Polish Notation
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to store numbers
        s = []

        # Loop through tokens and if number add to stack
        # if its operand, then perform operation on last 2 numbers in stack
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                b = s.pop()
                res = s.pop()
                if token == "+":
                    res += b
                elif token == "-":
                    res -= b
                elif token == "*":
                    res *= b
                elif token == "/":
                    res = int(res / b)
                s.append(res)
            else:
                s.append(int(token))

        return s[-1]
