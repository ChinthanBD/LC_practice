# https://leetcode.com/problems/detonate-the-maximum-bombs/
from typing import List
import collections
from math import sqrt

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        adjacency_list = collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = sqrt((x1-x2)**2 + (y1-y2)**2)

                # Check if bomb i can detonate bomb j
                if d <= r1:
                    adjacency_list[i].append(j)
                # Check if bomb j can detonate bomb i
                if d <= r2:
                    adjacency_list[j].append(i)

        def dfs(i, visited):
            if i not in visited:
                visited.add(i)
            
            for neighbour in adjacency_list[i]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
            return len(visited)
        
        res = float("-inf")
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        
        return res