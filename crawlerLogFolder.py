# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        mpp = {'../': -1, './': 0}
        ans = 0
        for operation in logs:
            ans += mpp.get(operation, 1)
            if ans <0:
                ans =0
        
        return ans if ans>0 else 0