"""
Solution of Linked List Cycle
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/linked-list-cycle/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        p1 moves 1 step ahead while p2 moves 2 steps ahead
        If a cycle is present, p1 is p2 == True will be attained as
        the while loop proceeds. If None is encountered in p1, p2, means
        there is no cycle
        """
        # Base case, if no item in linked list or only 1 item, means no cycle
        if not head or not head.next:
            return False
        p1, p2 = head, head

        # Loop continues while p1, p2 and p2.next are not None
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            # If p1 is p2, this means that loop is present
            if p1 is p2:
                return True

        return False
