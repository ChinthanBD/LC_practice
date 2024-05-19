#  https://bit.ly/3Cc8jlW

from collections import deque

class Solution:
    # Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = [[-1] * n for _ in range(m)]  # Initialize with -1 to indicate unvisited cells
        q = deque()
        visited = set()
        
        # Enqueue all cells containing '1' and set their distances to 0 in the ans matrix
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    q.append(((i, j), 0))  # Append the cell coordinates and initial distance
                    ans[i][j] = 0  # Distance to itself is 0
        
        # Perform BFS
        while q:
            (i, j), step = q.popleft()
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append(((ni, nj), step + 1))
                        ans[ni][nj] = step + 1  # Update distance in the answer grid
        
        return ans