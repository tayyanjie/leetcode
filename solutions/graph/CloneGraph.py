"""
Solution of Clone Graph
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/clone-graph/description/
"""

import queue


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        # v is a set to keep track new nodes whose
        # neighbors have been added
        v = set()
        d = {}
        # Dictionary with ref of original node as key
        # and new node as value
        d[node] = Node(node.val)

        q = queue.Queue()
        q.put(node)
        v.add(node.val)
        while not q.empty():
            curr = q.get()
            for neigh in curr.neighbors:
                # If the new node for neighbor has not been
                # craeted, create and add to d
                if neigh not in d:
                    d[neigh] = Node(neigh.val)
                # Add the neighbor node to neighbors of current node
                d[curr].neighbors.append(d[neigh])
                # If neighbor has not been visited to get all its
                # neighbors, add it to v and queue so that it can
                # have its neighbors added
                if neigh.val not in v:
                    q.put(neigh)
                    v.add(neigh.val)
        return d[node]
