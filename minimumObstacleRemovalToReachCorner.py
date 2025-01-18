# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        q = deque([(0,0,0)]) # r, c, obstacle
        visited = set([(0,0)])

        while q:
            r, c, obstacle = q.popleft()

            if r==ROW-1 and c==COL-1:
                return obstacle

            directions = [(0,1), (1,0),(-1,0),(0,-1)]

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if nr<0 or nc<0 or nc==COL or nr==ROW or (nr, nc) in visited:
                    continue
                
                if grid[nr][nc]:
                    q.append((nr, nc, obstacle+1))
                else:
                    q.appendleft((nr, nc, obstacle))

                visited.add((nr, nc))
