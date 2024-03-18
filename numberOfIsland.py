# https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1
import sys
from collections import deque
sys.setrecursionlimit(10**8)

class Solution:
    def __init__(self):
        self.visited = set()
        
    def bfs(self, i, j, m, n, grid):
        self.visited.add((i, j))
        queue = deque()
        queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for deli in range(-1, 2):
                for delj in range(-1, 2):
                    neighbouri = i + deli
                    neighbourj = j + delj
                    if 0 <= neighbouri < m and 0 <= neighbourj < n:
                        if (neighbouri, neighbourj) not in self.visited and grid[neighbouri][neighbourj]==1:
                            queue.append((neighbouri, neighbourj))
                            self.visited.add((neighbouri, neighbourj))
        
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in self.visited and grid[i][j]:
                    ans += 1
                    self.bfs(i, j, m, n, grid)
        
        return ans
