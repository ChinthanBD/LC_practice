# https://leetcode.com/problems/maximum-number-of-points-with-cost/?envType=daily-question&envId=2024-08-17
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        COLS = len(points[0])
        prev_row = points[0]

        for row in points[1:]:
            left = [0] * COLS
            right = [0] * COLS
            curr_row = [0] * COLS

            # Left to right pass
            left[0] = prev_row[0]
            for j in range(1, COLS):
                left[j] = max(left[j-1] - 1, prev_row[j])

            # Right to left pass
            right[COLS-1] = prev_row[COLS-1]
            for j in range(COLS-2, -1, -1):
                right[j] = max(right[j+1] - 1, prev_row[j])

            # Calculate the current row based on left and right passes
            for i in range(COLS):
                curr_row[i] = row[i] + max(left[i], right[i])

            prev_row = curr_row

        return max(prev_row)
