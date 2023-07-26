"""
Solution of Rotting Oranges
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/rotting-oranges/description/
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Perform BFS and determine max number of steps
        numFresh = 0
        q = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))  # x-coord, y-coord, steps

        ans = 0  # number of steps to make all rot

        # Perform BFS
        while len(q) > 0 and numFresh > 0:
            i, j, step = q.pop(0)
            # 3 means seen
            if grid[i][j] == 3:
                continue
            else:
                grid[i][j] = 3
            newSteps = step + 1

            # For each check in 4 directions,
            # update steps answer, update fruit to be rotten
            # reduce number of fresh fruit and add (i, j, newSteps) to queue

            # Check left
            if j > 0 and grid[i][j - 1] == 1:
                ans = max(ans, newSteps)
                grid[i][j - 1] = 2
                numFresh -= 1
                q.append((i, j - 1, newSteps))
            # Check right
            if j < n - 1 and grid[i][j + 1] == 1:
                ans = max(ans, newSteps)
                grid[i][j + 1] = 2
                numFresh -= 1
                q.append((i, j + 1, newSteps))
            # Check top
            if i > 0 and grid[i - 1][j] == 1:
                ans = max(ans, newSteps)
                grid[i - 1][j] = 2
                numFresh -= 1
                q.append((i - 1, j, newSteps))
            # Check bottom
            if i < m - 1 and grid[i + 1][j] == 1:
                ans = max(ans, newSteps)
                grid[i + 1][j] = 2
                numFresh -= 1
                q.append((i + 1, j, newSteps))

        # If q is empty and still have fresh fruit, not possible to make all rotten
        return ans if numFresh == 0 else -1
