# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()  # Stores indices of the elements
        ans = []
        
        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # Maintain elements in decreasing order in the deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            q.append(i)
            
            # Append the maximum element of the current window to the answer list
            if i >= k - 1:
                ans.append(nums[q[0]])
        
        return ans