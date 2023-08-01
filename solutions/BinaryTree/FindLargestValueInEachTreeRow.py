"""
Solution of Find Largest Value in Each Tree Row
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Peform BFS with layer number
        if not root:
            return []
        res = []
        q = deque()
        q.append((root, 0))

        while len(q) > 0:
            node, level = q.popleft()
            if len(res) < level + 1:
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return res
