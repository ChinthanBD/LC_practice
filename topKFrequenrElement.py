# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n,c in count.items():
            freq[c].append(n)
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

