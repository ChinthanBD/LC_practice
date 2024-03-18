# https://www.geeksforgeeks.org/problems/rotten-oranges2536/1
from collections import deque

class Solution:
    def findFreshCount(self, m, n, grid):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return True
        return False
                    
    # Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        queue = deque()
        visited = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((i, j, 0))  # Start time is 0
        time = 0
        while queue:
            i, j, t = queue.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighnouri = i + di
                neighnourj = j + dj
                if 0 <= neighnouri < m and 0 <= neighnourj < n and (neighnouri, neighnourj) not in visited:
                    if grid[neighnouri][neighnourj] == 1:
                        grid[neighnouri][neighnourj] = 2  # Update the orange to rotten
                        queue.append((neighnouri, neighnourj, t + 1))  # Increment time by 1 for the next level of rotten oranges
                        visited.add((neighnouri, neighnourj))  # Mark as visited
                        time = max(time, t + 1)  # Update the maximum time
        if self.findFreshCount(m, n, grid):  # If there are still fresh oranges left
            return -1
        return time