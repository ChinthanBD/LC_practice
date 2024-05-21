from typing import List

class Solution:
    def __init__(self):
        # Initialize the necessary variables
        self.visited = set()  # A set to keep track of visited cells
        self.ans = 0  # Variable to store the final count of enclaves
        self.m = 0  # Number of columns in the grid
        self.n = 0  # Number of rows in the grid
    
    def dfs(self, i, j, grid):
        # Perform an iterative depth-first search (DFS) starting from cell (i, j)
        stack = [(i, j)]
        while stack:
            ci, cj = stack.pop()  # Pop a cell from the stack
            if (ci, cj) not in self.visited:
                self.visited.add((ci, cj))  # Mark the cell as visited
                # Explore all 4 possible directions (right, down, left, up)
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni, nj = ci + di, cj + dj
                    # Check if the new cell is within bounds, is land, and not visited
                    if 0 <= ni < self.n and 0 <= nj < self.m and grid[ni][nj] == 1 and (ni, nj) not in self.visited:
                        stack.append((ni, nj))  # Add the cell to the stack for further exploration
        
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # Main function to count the number of enclaves in the grid
        self.visited.clear()  # Clear the visited set
        self.ans = 0  # Reset the answer counter
        self.n, self.m = len(grid), len(grid[0])  # Set the dimensions of the grid

        # Run DFS for all boundary cells with land (1)
        for i in range(self.n):
            if grid[i][0] == 1:  # Left boundary
                self.dfs(i, 0, grid)
            if grid[i][self.m - 1] == 1:  # Right boundary
                self.dfs(i, self.m - 1, grid)
                
        for j in range(self.m):
            if grid[0][j] == 1:  # Top boundary
                self.dfs(0, j, grid)
            if grid[self.n - 1][j] == 1:  # Bottom boundary
                self.dfs(self.n - 1, j, grid)
                
        # Count the remaining enclaves that are not connected to the boundary
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    self.ans += 1  # Increment the count for each enclave
                    
        return self.ans  # Return the final count of enclaves

