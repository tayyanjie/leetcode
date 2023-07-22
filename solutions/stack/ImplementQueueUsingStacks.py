"""
Solution of Implement Queue using Stacks
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/implement-queue-using-stacks/description/
"""


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Stacks 1 and 2
        self.s1 = []
        self.s2 = []

        # If top==1, means the front is in stack 1, else stack 2
        self.top = 1

        # keeps track the first element that pushed into stack 1
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # If s1 is empty, update the front of stack 1 with new element
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # All elements are in stack 1, so transfer all elements to stack 2
        # and get the last result
        if self.top == 1:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            # If there are elemenets in stack 2, then update the top to be stack 2
            if self.s2:
                self.top = 2
            return self.s1.pop()
        else:
            res = self.s2.pop()
            # Update top to stack 1 if stack 2 is empty
            if len(self.s2) == 0:
                self.top = 1
            return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        # the front element is at the top of stack 2
        if self.top == 2:
            return self.s2[-1]
        # if top is in stack1, just use the ref pointer
        else:
            return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2
