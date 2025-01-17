#https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]* n for _ in range(m)]

        def getMaxMovesFrom(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            max_moves=0
            directions_delta = [[-1,1],[0,1],[1,1]]
            for di, dj in directions_delta:
                newi, newj = i+di, j+dj
                if 0<=newi<m and 0<=newj<n and grid[newi][newj]>grid[i][j]:
                    max_moves=max(max_moves, 1+getMaxMovesFrom(newi, newj))
            dp[i][j] = max_moves 
            return dp[i][j]
        
        res = 0
        for i in range(m):
            res = max(res, getMaxMovesFrom(i, 0))
        
        return res
