"""
Solution of Flood Fill
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/flood-fill/description/
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original = image[sr][sc]
        m = len(image)
        n = len(image[0])

        # store pixels that have been filled
        filled = set()

        def fill(sr, sc, color):
            # If filled skip, else add coords to filled
            if (sr, sc) in filled:
                return
            else:
                filled.add((sr, sc))
            if image[sr][sc] == original:
                image[sr][sc] = color

                # Fill in 4 directions
                if sr > 0:
                    fill(sr - 1, sc, color)
                if sc > 0:
                    fill(sr, sc - 1, color)
                if sr < m - 1:
                    fill(sr + 1, sc, color)
                if sc < n - 1:
                    fill(sr, sc + 1, color)

        fill(sr, sc, color)
        return image
