# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        length = m * n

        l, r = 0, length -1

        while l<=r:

            mid = (l + r) // 2

            i, j = mid//n, mid % n

            if matrix[i][j] == target:
                return True
            elif target< matrix[i][j]:
                r = mid - 1
            else:
                l = mid + 1
        return False




