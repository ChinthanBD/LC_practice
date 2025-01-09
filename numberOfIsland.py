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


# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row_len = len(grid)
        col_len = len(grid[0])
        def bfs(row, col):
            q = deque([(row,col)])
            delta = [(0,1), (1,0), (-1,0), (0,-1)]
            visited.add((row,col))

            while q:
                r, c = q.popleft()
                for dr, dc in delta:
                    nr, nc = r+dr, c+dc

                    if 0<=nr<row_len and 0<=nr and 0<=nc<col_len and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))


        no_of_islands = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1' and (i, j) not in visited: 
                    bfs(i, j)
                    no_of_islands +=1

        return no_of_islands

