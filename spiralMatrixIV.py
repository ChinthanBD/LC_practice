https://leetcode.com/problems/spiral-matrix-iv/?envType=daily-question&envId=2024-09-09
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        
        current = head
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        d_idx = 0
        i, j = 0, 0

        while current:
            res[i][j] = current.val
            dx, dy = directions[d_idx]

            # If the next move is out of bounds or if it tries to march into a pre-existing cell, change directions.
            if i + dx < 0 or i + dx >= m or j + dy < 0 or j + dy >= n or res[i+dx][j+dy] > -1:
                d_idx = (d_idx + 1) % len(directions)
                dx, dy = directions[d_idx]

            i += dx
            j += dy 
            
            current = current.next
        
        return res



