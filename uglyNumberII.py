# https://leetcode.com/problems/ugly-number-ii/description/?envType=daily-question&envId=2024-08-18
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        minHeap = [1]
        visited = set()

        factors = [2, 3, 5]

        for i in range(n):
            num = heapq.heappop(minHeap)
            
            if i == n-1:
                return num
            
            for f in factors:
                if f * num not in visited:
                    visited.add(f*num)
                    heapq.heappush(minHeap, f*num)
            
