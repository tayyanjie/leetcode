"""
Solution of Insert Interval
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Base cases where either list is empty
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return list1

        # Set head
        if list1.val <= list2.val:
            head = list1
            p1 = list1.next  # pointer for list 1
            p2 = list2  # pointer for list 2
        else:
            head = list2
            p1 = list1
            p2 = list2.next
        curr = head

        # Iterate through all nodes and add to head accordingly
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if not p1 and not p2:
            return head
        # p2 is None
        elif p2:
            curr.next = p2
        # p1 is None
        else:
            curr.next = p1
        return head
