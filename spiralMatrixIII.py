# https://leetcode.com/problems/spiral-matrix-iii/submissions/1349191870/?envType=daily-question&envId=2024-08-08
from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Right, Down, Left, Up
        r, c = rStart, cStart
        res = []
        i = 0
        steps = 1

        while len(res) < rows * cols:
            for _ in range(2):  # Each direction gets repeated twice
                dr, dc = directions[i]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r, c = r + dr, c + dc
                i = (i + 1) % 4  # Move to the next direction
            steps += 1  # Increase the number of steps for the next iteration

        return res
