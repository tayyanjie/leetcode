"""
Solution of Min Stack
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/min-stack/description/
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # stores all the min values

    def push(self, val: int) -> None:
        # If min value or if the val <= last min value
        # then have to add to min stack
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        # If the popped value is <= min value in the stack
        # this means that the value should be removed from
        # min stack and the min value in stack will the next
        # min value in stack
        if popped <= self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
