https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=daily-question&envId=2024-07-19

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])
        col_max = []
        for j in range(n):
            max_ele = float("-inf")
            for i in range(m):
                max_ele = max(max_ele, matrix[i][j])
            col_max.append(max_ele)
        
        ans = []

        for i in range(m):
            for j in range(n):
                curr_ele = matrix[i][j]
                if curr_ele == row_min[i] and curr_ele == col_max[j]:
                    ans.append(curr_ele)
        
        return ans
