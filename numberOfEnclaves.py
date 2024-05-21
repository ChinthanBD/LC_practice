# https://bit.ly/3preQSc
from typing import List

class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = 0
        self.m = 0
        self.n = 0
    
    def dfs(self, i, j, grid):
        stack = [(i, j)]
        while stack:
            ci, cj = stack.pop()
            if (ci, cj) not in self.visited:
                self.visited.add((ci, cj))
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < self.n and 0 <= nj < self.m and grid[ni][nj] == 1 and (ni, nj) not in self.visited:
                        stack.append((ni, nj))
        
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        self.visited.clear()
        self.ans = 0
        self.n, self.m = len(grid), len(grid[0])

        # Run DFS for all boundary cells with land (1)
        for i in range(self.n):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid)
            if grid[i][self.m - 1] == 1:
                self.dfs(i, self.m - 1, grid)
                
        for j in range(self.m):
            if grid[0][j] == 1:
                self.dfs(0, j, grid)
            if grid[self.n - 1][j] == 1:
                self.dfs(self.n - 1, j, grid)
                
        # Count the remaining enclaves
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    self.ans += 1
                    
        return self.ans