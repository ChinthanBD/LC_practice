class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize the boundaries of the matrix
        left, right = 0, len(matrix[0]) - 1  # Left and right boundaries for columns
        top, bottom = 0, len(matrix) - 1     # Top and bottom boundaries for rows
        
        res = []  # List to store the result in spiral order
        
        # Continue looping until the boundaries meet or overlap
        while left <= right and top <= bottom:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Move the right boundary left

            # Check if there are rows remaining to traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up

            # Check if there are columns remaining to traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # Move the left boundary right
        
        return res  # Return the list of elements in spiral order



############################################## Destructive approach########################
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return []

        while matrix:

            res += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    if row:
                        res.append(row.pop())
                
            if matrix:
                res+=matrix.pop()[::-1]
            
            if matrix:
                for row in matrix[::-1]:
                    if row:
                        res.append(row.pop(0))
            
        return res
