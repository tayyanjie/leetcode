"""
Solution of K Closest Points to Origin
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/k-closest-points-to-origin/description/
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This solution uses sorting. Alternatively, a min heap can be used
        def distance(x1, y1):
            return (x1**2 + y1**2) ** 0.5

        distances = [(distance(x1, y1), (x1, y1)) for x1, y1 in points]
        distances.sort(key=lambda x: x[0])

        return [x[1] for x in distances[:k]]
