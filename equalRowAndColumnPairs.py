# https://leetcode.com/problems/equal-row-and-column-pairs/submissions/1395298261/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = {}
        
        # Count occurrences of each row
        for row in grid:
            # Convert row to a tuple (to make it hashable)
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1
        
        result = 0
        
        # Check each column against the row counts
        for j in range(n):
            column = [grid[i][j] for i in range(n)]
            column_tuple = tuple(column)
            if column_tuple in row_count:
                result += row_count[column_tuple]
        
        return result
