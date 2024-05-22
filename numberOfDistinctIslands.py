https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1
import sys
from typing import List, Tuple, Set

# Increase the recursion limit for large grids
sys.setrecursionlimit(10**8)

class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, base_x: int, base_y: int) -> List[Tuple[int, int]]:
            stack = [(x, y)]
            shape = []
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) not in visited:
                    visited.add((cx, cy))
                    shape.append((cx - base_x, cy - base_y))  # Record relative position
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Four possible directions
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in visited:
                            stack.append((nx, ny))
            return shape

        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        visited = set()
        unique_islands = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island_shape = dfs(i, j, i, j)
                    unique_islands.add(tuple(island_shape))  # Convert list of tuples to a tuple

        return len(unique_islands)