"""
Solution of Invert Binary Tree
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/invert-binary-tree/description/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # Swap the left and right trees
        root.left, root.right = root.right, root.left

        # Invert the left tree
        if root.left:
            self.invertTree(root.left)

        # Invert the right tree
        if root.right:
            self.invertTree(root.right)
        return root
