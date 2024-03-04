# https://leetcode.com/problems/n-queens/submissions/1192927152/
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negativeDiag = set()
        board = [['.'] * n for i in range(n)]
        ans = []
        def backtrack(r):

            if r == n:
                ans.append([''.join(r) for r in board])
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negativeDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negativeDiag.add(r-c)
                board[r][c] = 'Q'
                
                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negativeDiag.remove(r-c)
                board[r][c] = '.'
        
        backtrack(0)
        return ans
        