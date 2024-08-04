# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels_mpp = set()
        ans = 0
        for j in jewels:
            jewels_mpp.add(j)
        
        for s in stones:
            if s in jewels_mpp:
                ans +=1
        
        return ans 
