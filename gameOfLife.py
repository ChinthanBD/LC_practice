# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        res = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = board[i][j]

        
        for i in range(m):
            for j in range(n):
                live_count = 0
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    neighbour_i = i + di
                    neighbour_j = j + dj
                    if 0<=neighbour_i<m and 0<=neighbour_j<n:
                        if board[neighbour_i][neighbour_j] == 1:
                            live_count +=1
                if board[i][j] == 1:
                    if live_count <2 or live_count >3:
                        res[i][j] = 0
                else:
                    if live_count == 3:
                        res[i][j] = 1

        
        for i in range(m):
            for j in range(n):
                board[i][j] = res[i][j]
                    