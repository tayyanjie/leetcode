"""
Solution of Number of Islands
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/number-of-islands/description/
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Perform BFS to identify all cordinates related to a single coordinate with
        "1". This forms one island. Add all these coordinates to seen so that
        they are not explored again. Repeat for all coords in grid to obtain count
        of islands.
        """
        m, n = len(grid), len(grid[0])

        # matrix to store whether coordinate has been searched
        seenGrid = [n * [0] for i in range(m)]

        def bfs(i, j):
            """
            Perform BFS, finding all 1 coordinates that form an island
            with coordinates (i, j) and add all of them to seen.
            """
            q = [(i, j)]
            while len(q) > 0:
                i, j = q.pop(0)
                if seenGrid[i][j]:
                    continue
                else:
                    seenGrid[i][j] = 1
                # check left
                if j > 0 and not seenGrid[i][j - 1] and grid[i][j - 1] == "1":
                    q.append((i, j - 1))
                # check right
                if j < n - 1 and not seenGrid[i][j + 1] and grid[i][j + 1] == "1":
                    q.append((i, j + 1))
                # check top
                if i > 0 and not seenGrid[i - 1][j] and grid[i - 1][j] == "1":
                    q.append((i - 1, j))
                # check bottom
                if i < m - 1 and not seenGrid[i + 1][j] and grid[i + 1][j] == "1":
                    q.append((i + 1, j))

        # Store number of islands
        count = 0

        # Loop through all cordinates, if not seen before and is "1"
        # new island is found so increment count and perform BFS
        # to add all related "1" to seen.
        for i in range(m):
            for j in range(n):
                if not seenGrid[i][j] and grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count
