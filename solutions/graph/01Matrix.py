"""
Solution of 01 Matrix
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/01-matrix/description/
"""

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Use deque for BFS
        q = deque()

        for i in range(m):
            for j in range(n):
                # Add all start points i.e., those with 0 to deque
                # which are the src for BFS
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                # Otherwise, set as -1, indicating that the coords
                # has not been seen during BFS
                else:
                    mat[i][j] = -1

        total_elements = m * n

        # count used to keep track the number of coordinates
        # that have not been through the while loop
        # If count 0 means all coords seen and can return result
        count = total_elements

        while len(q) > 0:
            i, j, dist = q.popleft()

            # -1 means not seen and 0 means src
            # if its src, cannot skip loop so as to decrease count
            if mat[i][j] != -1 and mat[i][j] != 0:
                continue

            # Set distance
            mat[i][j] = dist
            count -= 1

            if count == 0:
                return mat

            # The distances of adjacent unseen will have dist + 1
            dist += 1

            # add top
            if i > 0:
                if mat[i - 1][j] == -1:
                    q.append((i - 1, j, dist))

            # add bottom
            if i < m - 1:
                if mat[i + 1][j] == -1:
                    q.append((i + 1, j, dist))

            # add left
            if j > 0:
                if mat[i][j - 1] == -1:
                    q.append((i, j - 1, dist))

            # add right
            if j < n - 1:
                if mat[i][j + 1] == -1:
                    q.append((i, j + 1, dist))

        return mat
