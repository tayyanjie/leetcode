"""
Solution of Binary Tree Level Order Traversal
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Queue for BFS, each element is (node, level)
        # level to keep track of whether to add node.val to next level
        # in result
        q = [(root, 0)]
        result = []
        while len(q) > 0:
            # perform BFS
            node, level = q.pop(0)
            # If condition checks if list for level has been added to result
            if len(result) < level + 1:
                result.append([node.val])
            else:
                result[level].append(node.val)
            # Add the left and right nodes to queue
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return result
