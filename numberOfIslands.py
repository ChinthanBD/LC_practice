# https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1
import sys

# Set the recursion limit to avoid "RecursionError: maximum recursion depth exceeded" for large grids
sys.setrecursionlimit(10**8)

class Solution:
    def numIslands(self, grid):
        # Get the number of rows and columns in the grid
        rows = len(grid)
        columns = len(grid[0])

        # Function to return the neighbors of a given node
        def return_neighbours(node):
            # Unpack the coordinates of the node
            i, j = node
            # Define the possible neighbor indices including diagonals
            possible_neighbour_index = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            neighbours = []

            # Iterate over possible neighbor indices
            for di, dj in possible_neighbour_index:
                # Calculate the coordinates of the potential neighbor
                ni, nj = i + di, j + dj
                # Check if the potential neighbor is within the bounds of the grid
                if 0 <= ni < rows and 0 <= nj < columns:
                    # If it is, add it to the list of neighbors
                    neighbours.append((ni, nj))
            return neighbours

        # Depth-first search (DFS) function to explore the connected components (islands)
        def dfs(node):
            # Mark the node as visited
            if node not in visited:
                visited.add(node)
                # Unpack the coordinates of the node
                i, j = node
                # Iterate over the neighbors of the current node
                for ni, nj in return_neighbours((i, j)):
                    # Check if the neighbor is land (1) and not visited yet
                    if grid[ni][nj] == 1 and (ni, nj) not in visited:
                        # If it is, recursively explore the neighbor
                        dfs((ni, nj))

        # Set to keep track of visited nodes
        visited = set()
        # Variable to store the count of islands
        island_count = 0

        # Iterate over each cell in the grid
        for row in range(rows):
            for column in range(columns):
                # If the cell is land (1) and not visited yet, start DFS from that cell
                if grid[row][column] == 1 and (row, column) not in visited:
                    dfs((row, column))
                    # Increment the island count after exploring all land cells in the connected component
                    island_count += 1

        # Return the total count of islands
        return island_count
