# https://www.naukri.com/code360/problems/ninja-and-his-friends_3125885?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from typing import List

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # Memoization table
    memo = {}

    def findMax(i, j1, j2):
        # Check if the position is out of bounds
        if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
            return float('-inf')

        # If we've reached the last row
        if i == r - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        # Check if the result is already computed
        if (i, j1, j2) in memo:
            return memo[(i, j1, j2)]

        # Initialize the max chocolates
        max_chocolates = float('-inf')

        # Explore all possible moves for both robots
        for dj1 in range(-1, 2):
            for dj2 in range(-1, 2):
                curr_chocolates = grid[i][j1]
                if j1 != j2:
                    curr_chocolates += grid[i][j2]
                curr_chocolates += findMax(i + 1, j1 + dj1, j2 + dj2)
                max_chocolates = max(max_chocolates, curr_chocolates)

        memo[(i, j1, j2)] = max_chocolates
        return max_chocolates

    return findMax(0, 0, c - 1)


