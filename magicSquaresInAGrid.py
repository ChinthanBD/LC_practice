# https://leetcode.com/problems/magic-squares-in-grid/
from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0

        def magic(r, c):
            # Collect all values in the 3x3 grid
            vals = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in vals or not (1 <= grid[i][j] <= 9):
                        return 0
                    vals.add(grid[i][j])

            # Check the rows
            for i in range(r, r + 3):
                if sum(grid[i][c: c + 3]) != 15:
                    return 0

            # Check the columns
            for i in range(c, c + 3):
                if grid[r][i] + grid[r + 1][i] + grid[r + 2][i] != 15:
                    return 0

            # Check the diagonals
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
                return 0

            return 1

        for r in range(ROWS - 2):
            for c in range(COLS - 2):
                ans += magic(r, c)

        return ans
