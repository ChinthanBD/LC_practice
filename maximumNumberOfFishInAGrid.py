# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])

        # Depth First Search function to calculate fish count in a connected area
        def dfs(i, j):
            # Boundary and visited checks
            if i < 0 or j < 0 or i == ROW or j == COL or (i, j) in visited or grid[i][j] == 0:
                return 0

            res = grid[i][j]  # Start with current cell's fish count
            visited.add((i, j))  # Mark cell as visited

            # Explore all 4 directions
            for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                res += dfs(i + di, j + dj)

            return res

        ans = 0
        # Iterate over all cells in the grid
        for i in range(ROW):
            for j in range(COL):
                # If the cell is not visited and contains fish, start DFS
                if (i, j) not in visited and grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))  # Update the maximum fish count

        return ans
