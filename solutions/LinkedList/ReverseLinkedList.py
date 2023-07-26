"""
Solution of Reverse Linked List
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/reverse-linked-list/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If no node or only 1 node in list, return head
        if not head or not head.next:
            return head
        # Get first 2 nodes
        a, b = head, head.next
        # First node will be last node
        a.next = None
        # If only 2 nodes, just reverse
        if not b.next:
            b.next = a
            return b
        # Otherwise, get 3rd node
        c = b.next
        # 2nd node next should be first node
        b.next = a

        # While c is not last node in list
        while c.next is not None:
            # shift the window of a, b and c by 1 node
            a, b, c = b, c, c.next
            # reverse the pointer
            b.next = a

        # reverse the final pointer
        c.next = b

        return c
