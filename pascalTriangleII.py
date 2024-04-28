# https://leetcode.com/problems/pascals-triangle-ii/description/
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # The first row is always [1]

        for i in range(1, rowIndex + 1):
            # Generate the next row based on the previous row
            next_row = [1]  # Leftmost element is always 1
            for j in range(1, i):
                next_row.append(row[j - 1] + row[j])
            next_row.append(1)  # Rightmost element is always 1
            row = next_row
        
        return row
