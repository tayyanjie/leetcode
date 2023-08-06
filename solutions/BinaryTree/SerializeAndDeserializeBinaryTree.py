"""
Solution of Serialize and Deserialize Binary Tree
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # Store tree as dictionary with index
        # as key and value as value of node
        # left node of a parent node has ind*2
        # and righ tnode has ind*2 + 1 where
        # ind of parent node is ind
        res = {}

        def dfs(node, ind):
            res[ind] = node.val
            if node.left:
                dfs(node.left, 2 * ind)
            if node.right:
                dfs(node.right, 2 * ind + 1)

        dfs(root, 1)

        # Convert dictionary to string format
        res = [f"{ind}:{res[ind]}" for ind in res]
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        # rebuild dictionary from serialize step
        nodes = {}
        for s in data.split(","):
            ind, val = s.split(":")
            ind, val = int(ind), int(val)
            nodes[ind] = val

        # Create tree from dictionary
        root = TreeNode(nodes[1])

        def addNodes(node, ind):
            if 2 * ind in nodes:
                node.left = TreeNode(nodes[2 * ind])
                addNodes(node.left, 2 * ind)
            if 2 * ind + 1 in nodes:
                node.right = TreeNode(nodes[2 * ind + 1])
                addNodes(node.right, 2 * ind + 1)

        addNodes(root, 1)
        return root
