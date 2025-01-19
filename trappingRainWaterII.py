# https://leetcode.com/problems/trapping-rain-water-ii/


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        ROW = len(heightMap)
        COL = len(heightMap[0])
        minheap = []
        visited = set()
        for i in range(ROW):
            for j in range(COL):
                if i in [0, ROW-1] or j in [0, COL-1]:
                    heappush(minheap, (heightMap[i][j], i, j))
                    visited.add((i, j))    

        maxHeight = -1
        res = 0
        while minheap:
            height, r, c = heappop(minheap)

            maxHeight = max(maxHeight, height)
            res += maxHeight - height

            delta = [(0,1),(1,0),(0,-1),(-1,0)]

            for dr, dc in delta:
                nr, nc = r+dr, c+dc

                if (nr<0 or nc<0 or nr>=ROW or nc>=COL or (nr, nc) in visited):
                    continue
                
                heappush(minheap, (heightMap[nr][nc], nr, nc))
                visited.add((nr, nc)) 
        
        return res
