# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=daily-question&envId=2025-01-18

from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: (0, 1),   # Right
            2: (0, -1),  # Left
            3: (1, 0),   # Down
            4: (-1, 0)   # Up
        }
        ROW, COL = len(grid), len(grid[0])

        q = deque([(0, 0, 0)])  # (r, c, cost)
        visited = {(0, 0): 0}

        while q:
            r, c, cost = q.popleft()

            if (r, c) == (ROW - 1, COL - 1):
                return cost

            for d, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROW and 0 <= nc < COL:
                    n_cost = cost if d == grid[r][c] else cost + 1
                    if visited.get((nr, nc), float('inf')) > n_cost:
                        visited[(nr, nc)] = n_cost
                        if d == grid[r][c]:
                            q.appendleft((nr, nc, n_cost))  # Prioritize no-cost moves
                        else:
                            q.append((nr, nc, n_cost))  # Add cost moves later

        return -1  # If unreachable
