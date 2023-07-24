"""
Solution of Course Schedule
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/course-schedule/description/
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Use Kahn Algorithm for topological sort
        If number of visited by Kahn's algorithm > numCourses, this means that
        cycle is present. Start from nodes with indegree of 0 and decrement
        the indegree of neighbours. Repeat until no nodes in queue. If number of visited
        is eqaul to numCourses, this means no cycle. If cycle is present,
        the indegree of some nodes will not be zeroed and visited will be < numCourses.
        """
        # List to store the indegree of each course
        indegree = numCourses * [0]

        # adj[i] = set containing courseNum of ajdacent nodes
        adj = [set() for i in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            adj[a].add(b)
            adj[b].add(a)
        q = []

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        visited = 0

        while len(q) > 0:
            course = q.pop(0)
            visited += 1
            if visited > numCourses or visited + len(q) > numCourses:
                return False
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return visited == numCourses
