"""
Solution of Balanced Binary Tree
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/balanced-binary-tree/description/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            """
            Returns depth, and whether subtree beginning from root is balanced
            """
            if not root:
                return 0, True

            # Check whether left subtree is balanced and obtain depth
            if root.left:
                left_depth, left_is_balanced = helper(root.left)
            else:
                left_depth, left_is_balanced = 0, True

            # If not balanced, then no need to proceed to checking right subtree
            # because if left subtree is not height balanced, then entire tree isn't
            if not left_is_balanced:
                return 0, False
            if root.right:
                right_depth, right_is_balanced = helper(root.right)
            else:
                right_depth, right_is_balanced = 0, True

            # Do the same check regarding height balance for right subtree
            if not right_is_balanced:
                return 0, False

            # Check that tree from root is height balanced
            is_balanced = abs(left_depth - right_depth) <= 1

            # Depth of tree from root is 1 + max depth of left and right subtree.
            return 1 + max(left_depth, right_depth), is_balanced

        return helper(root)[1]
