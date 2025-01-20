# https://leetcode.com/problems/first-completely-painted-row-or-column

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROW = len(mat)
        COL = len(mat[0])
        n = len(arr)

        index_val_mpp = {}

        for i in range(ROW):
            for j in range(COL):
                index_val_mpp[mat[i][j]] = (i,j)
        
        row_count = {}
        col_count = {}

        for i in range(len(arr)):
            r, c = index_val_mpp.get(arr[i])

            row_count[r] = row_count.get(r, 0) + 1
            col_count[c] = col_count.get(c, 0) + 1

            if row_count[r] == COL or col_count[c] == ROW:
                return i
    
