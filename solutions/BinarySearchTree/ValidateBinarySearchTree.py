"""
Solution of Validate Binary Search Tree
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/validate-binary-search-tree/description/
"""

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = []
        # (node, minValue left subtree must be greater than, maxValue right subtree must be < than)
        # For root, no minVal and maxVal restriction
        q.append((root, -inf, inf))
        while len(q) > 0:
            node, minVal, maxVal = q.pop(0)
            if node.left:
                if node.left.val >= node.val or node.left.val <= minVal:
                    return False
                else:
                    # For left subtree, all values must be less than current node val
                    q.append((node.left, minVal, node.val))
            if node.right:
                if node.right.val <= node.val or node.right.val >= maxVal:
                    return False
                else:
                    # For right subtree, all values must be greater than current node val
                    q.append((node.right, node.val, maxVal))
        return True
