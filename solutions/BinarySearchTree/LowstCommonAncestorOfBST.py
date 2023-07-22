"""
Solution of Lowest Common Ancestor of a Binary Search Tree
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Determine the small and large values between p and q
        if p.val <= q.val:
            small, big = p, q
        else:
            small, big = q, p

        def getLCA(root, small, big):
            if small is root or big is root:
                return root
            # If the small value < root and large value > root, means root is LCA
            if small.val < root.val and big.val > root.val:
                return root
            # If both small and large value < root, search the left subtree
            if small.val <= root.val and big.val <= root.val:
                return getLCA(root.left, small, big)
            # Else search the right subtree
            else:
                return getLCA(root.right, small, big)

        return getLCA(root, small, big)
