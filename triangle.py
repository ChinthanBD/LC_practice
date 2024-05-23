from os import *
from sys import *
from collections import *
from math import *

def minimumPathSum(triangle, n):
    # Initialize current and next rows to store the minimum path sums
    curr_row = [0] * n
    next_row = [0] * n
    
    # Initialize the next_row with the values from the last row of the triangle
    for i in range(n):
        next_row[i] = triangle[n-1][i]
    
    # Iterate from the second last row to the first row
    for i in range(n-2, -1, -1):
        for j in range(i + 1):
            down = triangle[i][j] + next_row[j]
            diagonal = triangle[i][j] + next_row[j+1]
            curr_row[j] = min(down, diagonal)
        
        # Copy current row to next row for the next iteration
        next_row = curr_row[:]
    
    return next_row[0]